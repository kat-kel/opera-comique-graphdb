from datetime import date
import calendar

from opera_comique_api.database.connection import conn
from opera_comique_api.models.results import SimpleResult


def get_month_range(year: int, month: int) -> tuple[date]:
    last_day = calendar.monthrange(year, month)[-1]
    last_date = date(year, month, last_day)
    first_date = date(year, month, 1)
    return first_date, last_date


def performances_in_month(year: int, month: int):
    """
    Read performances of works in a month.

    Args:
        year (int): A year within the scope of the database's records.
        month (int): Month, between 1 and 12.
    """
    start, end = get_month_range(year=year, month=month)

    match_stmt, return_stmt = SimpleResult._statements()
    query = f"""{match_stmt}
WHERE p.date >= date("{start}")
AND p.date <= date("{end}")
AND p.location = "Opéra-Comique"
{return_stmt} ORDER BY p.date
"""
    response = conn.execute(query)
    count = response.get_num_tuples()

    results = []
    while response.has_next():
        row = response.get_next()[0]
        r = SimpleResult.model_validate(row)
        results.append(r)
    return {"count": count, "items": results, "q": query}


def performances_on_day(year: int, month: int, day: int):
    """
    Read performances of works on a specific day.

    Args:
        year (int): A year within the scope of the database's records.
        month (int): Month, between 1 and 12.
        day (int): Day within the month.
    """
    match_stmt, return_stmt = SimpleResult._statements()

    d = date(year, month, day)
    query = f"""{match_stmt}
WHERE p.date = date("{d}") AND p.location = "Opéra-Comique"
{return_stmt}
"""
    response = conn.execute(query)
    count = response.get_num_tuples()

    results = []
    while response.has_next():
        row = response.get_next()[0]
        r = SimpleResult.model_validate(row)
        results.append(r)
    return {"count": count, "items": results, "q": query}
