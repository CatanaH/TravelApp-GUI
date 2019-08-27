import unittest
from TravelApp2 import verify_month, verify_day, verify_year

class MyTestCase(unittest.TestCase):
    def test_verify_month(self):
        mon = 'jan'
        mon = verify_month(mon)
        self.assertEqual(mon, 'Jan')

    def test_verify_month1(self):
        mon = 'jac'
        mon = verify_month(mon)
        self.assertEqual(mon, '')

    def test_verify_day(self):
        day = 12
        day = verify_day(day)
        self.assertEqual(day, 12)

    def test_verify_year(self):
        year = 20
        year = verify_year(year)
        self.assertEqual(year, 20)


if __name__ == '__main__':
    unittest.main()
