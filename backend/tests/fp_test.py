import unittest
from datetime import date

from pydantic import BaseModel

from opera_comique_api.database import Connection



class Test(unittest.TestCase):
    def test(self):
        conn = Connection(PROD_ENV="0")
        response = 

       


if __name__ == "__main__":
    unittest.main()
