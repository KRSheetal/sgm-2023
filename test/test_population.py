import unittest
from unittest import TestCase
import population

class TestPopulation(TestCase):


    def test_population_of_each_state(self):
        expected_population = '732673'
        state = 'Minnesota'
        result = population.get_population(state)
        self.assertEqual(expected_population, result)


if __name__ == 'main':
    unittest.main()
