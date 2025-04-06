from kuzu import Connection

from opera_comique_api import DATADIR

PERFORMANCE_NODE_CSV = DATADIR.joinpath("performance_nodes.csv").absolute()

CREATE_PERFORMANCE_NODE_TABLE = f"""
CREATE NODE TABLE Performance (
    date DATE,
    location STRING,
    PRIMARY KEY(date)
);
COPY Performance FROM "{PERFORMANCE_NODE_CSV}" (header=true);
"""

WORK_NODE_CSV = DATADIR.joinpath("work_nodes.csv").absolute()

CREATE_WORK_NODE_TABLE = f"""
CREATE NODE TABLE Work (
    charlton_id STRING,
    title STRING,
    PRIMARY KEY (charlton_id)
);
COPY Work FROM "{WORK_NODE_CSV}" (header=true);
"""

PERFORMANCE_EDGE_CSV = DATADIR.joinpath("is_performed_edge.csv").absolute()

CREATE_PERFORMANCE_REL_TABLE = f"""
CREATE REL TABLE IS_PERFORMED (
    FROM Work TO Performance,
    source STRING
);
COPY IS_PERFORMED FROM "{PERFORMANCE_EDGE_CSV}" (header=true);
"""


def create_tables(conn: Connection) -> None:
    conn.execute(
        """
        DROP TABLE IF EXISTS IS_PERFORMED;
        DROP TABLE IF EXISTS Work;
        DROP TABLE IF EXISTS Performance;
        """
    )
    conn.execute(CREATE_PERFORMANCE_NODE_TABLE)
    conn.execute(CREATE_WORK_NODE_TABLE)
    conn.execute(CREATE_PERFORMANCE_REL_TABLE)
