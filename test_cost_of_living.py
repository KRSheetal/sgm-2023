from unittest import TestCase

import cost_of_living

class TestCost_of_living(TestCase):

    def test_cost_of_living(self):
        city = 'minneapolis'
        state = 'minnesota'
        location = city, state
        result = cost_of_living.get_cost_of_living(location)
        expected = 7359
        self.assertEqual(expected, result)

