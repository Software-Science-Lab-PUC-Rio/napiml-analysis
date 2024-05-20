import unittest
from utils.bootstrapping import BootstrappingUtils

class TestBootstrapping(unittest.TestCase):
    def test_bootstrapping_single(self):
        """
            Test to check if given a set of answered single option questions
            we can have apply bootstrapping technique to infer population
            behavior. 
        """
        
        test_bootstrapping_utils = BootstrappingUtils(['Valor 1'], ['Valor 1', 'Valor 2'], 2, 2)
        test_population_metric = {'Valor 1': {'population': [100.0, 100.0], 'confidence': (100.0, 100.0, 100.0)},
                                  'Valor 2': {'population': [0.0, 0.0], 'confidence': (0.0, 0.0, 0.0)}}

        self.assertEqual(test_bootstrapping_utils.bootstrapping('single'), test_population_metric)


    def test_bootstrapping_multiple(self):
        """
            Test to check if given a set of answered multiple option questions
            we can have apply bootstrapping technique to infer population
            behavior. 
        """
        
        test_bootstrapping_utils = BootstrappingUtils([['Valor 1']], ['Valor 1', 'Valor 2'], 4, 4)
        test_population_metric = {'Valor 1': {'population': [100.0, 100.0, 100.0, 100.0], 'confidence': (100.0, 100.0, 100.0)},
                                  'Valor 2': {'population': [0.0, 0.0, 0.0, 0.0], 'confidence': (0.0, 0.0, 0.0)}}

        self.assertEqual(test_bootstrapping_utils.bootstrapping('multiple'), test_population_metric)


    def test_bootstrapping_numerical_fields(self):
        """
            Test to check if given a set of answered numerical field questions
            we can have apply bootstrapping technique to infer population
            behavior. 
        """
        
        test_bootstrapping_utils = BootstrappingUtils([10, 10, 10], [], 3, 3)
        test_population_metric = {'population': [10, 10, 10], 'confidence': (10.0, 10.0, 10.0)}

        self.assertEqual(test_bootstrapping_utils.bootstrapping_numerical_fields(), test_population_metric)
