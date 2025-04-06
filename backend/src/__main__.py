import uvicorn
import os


def dev():
    """Launched with `poetry run start` at root level"""
    os.environ["FASTAPI_PROD"] = "0"
    uvicorn.run(
        "opera_comique_api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


def prod():
    """Launched with `poetry run start` at root level"""
    os.environ["FASTAPI_PROD"] = "1"
    uvicorn.run(
        "opera_comique_api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
    )
