from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent

DB = PROJECT_ROOT.joinpath("graph_db")
DATADIR = PROJECT_ROOT.joinpath("data")
