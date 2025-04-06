from datetime import date

from opera_comique_api.database.connection import conn
from opera_comique_api.models.results import SimpleResult


def work_performances(charlton_id: str) -> dict:
    """
    Read performances of a given work.

    Args:
        charlton_id (str): Charlton ID of the work.
    """
    match_stmt, return_stmt = SimpleResult._statements()

    query = f"""{match_stmt}
WHERE w.charlton_id = '{charlton_id}'
{return_stmt} ORDER BY p.date
"""
    response = conn.execute(query)
    count = response.get_num_tuples()

    results = []
    while response.has_next():
        row = response.get_next()[0]
        print(row)
        r = SimpleResult.model_validate(row)
        results.append(r)

    return {"count": count, "items": results, "q": query}


def work_performances_in_range(
    charlton_id: str,
    start: int,
    end: int,
) -> dict:
    match_stmt = SimpleResult._match()

    start = date.fromisocalendar(start, 1, 1)
    end += 1
    end = date.fromisocalendar(end, 1, 1)

    query = f"""{match_stmt}
WHERE w.charlton_id = '{charlton_id}'
AND p.date >= date("{start}")
AND p.date < date("{end}")
RETURN count(p)
"""
    response = conn.execute(query)

    while response.has_next():
        result = response.get_next()[0]
        break
    return {"count": result, "q": query}
