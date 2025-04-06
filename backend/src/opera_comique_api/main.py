from fastapi import FastAPI

from opera_comique_api.routes.performances.work import (
    work_performances,
    work_performances_in_range,
)
from opera_comique_api.routes.performances.year import (
    performances_in_month,
    performances_on_day,
)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "server online"}


@app.get("/performances/work/{charlton_id}")
def read_performances_of_work(charlton_id):
    work_performances(charlton_id=charlton_id)


@app.get("/performances/work/{charlton_id}/years/{start}-{end}/")
def read_performances_of_work_in_range(charlton_id, start, end):
    work_performances_in_range(charlton_id=charlton_id, start=start, end=end)


@app.get("/performances/{year}/{month}")
def read_performances_in_month(year, month):
    performances_in_month(year=year, month=month)


@app.get("/performances/{year}/{month}/{day}")
def read_performances_in_day(year, month, day):
    performances_on_day(year=year, month=month, day=day)
