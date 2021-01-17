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


if __name__ == '__main__':
    unittest.main()
