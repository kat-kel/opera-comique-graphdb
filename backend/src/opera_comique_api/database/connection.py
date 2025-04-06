import os
import shutil
from pathlib import Path
from typing import Any

import kuzu
from kuzu import PreparedStatement, QueryResult

from opera_comique_api import DB
from opera_comique_api.database.tables import create_tables

PROD_ENV = os.environ.get("FASTAPI_PROD")


class Connection:

    def __init__(
        self,
        db_path: Path = DB,
        read_only: bool = True,
        PROD_ENV: str = PROD_ENV,
    ):
        if PROD_ENV == "0":
            self._start_db_from_new(db_path=db_path)
            read_only = False
        db = kuzu.Database(db_path, read_only=read_only)
        self.conn = kuzu.Connection(db)

    @classmethod
    def _start_db_from_new(cls, db_path: Path):
        if db_path.is_dir():
            shutil.rmtree(db_path)
        db = kuzu.Database(db_path)
        conn = kuzu.Connection(db)
        create_tables(conn=conn)

        conn.close()

    def execute(
        self,
        query: str | PreparedStatement,
        parameters: dict[str, Any] | None = None,
    ) -> QueryResult | list[QueryResult]:
        return self.conn.execute(query=query, parameters=parameters)


conn = Connection()
