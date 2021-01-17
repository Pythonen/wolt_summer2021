import unittest
import utils


class TestUtilityMethods(unittest.TestCase):

    def test_getLatLonInKm_same_spot(self):
        result = utils.getDistanceFromLatLonInKm(
            24.951305, 60.175722, 24.951305, 60.175722)
        self.assertEqual(result, 0)

    def test_getLatLonInKm_over_acceptable_dist(self):
        result = utils.getDistanceFromLatLonInKm(
            60.169857, 24.938379, 62.242561, 25.747499)
        self.assertEqual(result, None)

    def test_getLatLonInKm_acceptable_dist(self):
        result = utils.getDistanceFromLatLonInKm(
            62.242561, 25.747499, 62.242350, 25.726155)
        self.assertEqual(int(result), 1)

    def test_is_4months_not(self):
        self.assertEqual(utils.is_older_than_4mo('2021-01-01'), False)

    def test_is_4months_is(self):
        self.assertEqual(utils.is_older_than_4mo('2020-02-02'), True)


if __name__ == '__main__':
    unittest.main()
