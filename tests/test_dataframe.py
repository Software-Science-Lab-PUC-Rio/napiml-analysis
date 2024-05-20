import unittest
import pandas as pd
import pandas.testing as pd_testing
from utils.dataframe import DataframeUtils

class TestBasic(unittest.TestCase):
    def test_remove_columns(self):
        """
            Test if we can remove some columnsgiven a CSV file, a file containing
            columns to remove and a file containing the formatted columns names 
            for the ones which were not removed.
        """
        test_dataframe_utils = DataframeUtils('./tests/df_test.csv', ';', './tests/unused_columns.txt', './tests/formatted_columns.txt')
        # the index is not important, but when we internally format df we need to reset index
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)
        test_dataframe_utils.remove_columns(['Coluna_C'])

        test_result_dataframe = pd.DataFrame()
        test_result_dataframe['Coluna_A'] = ['1', '2']
        test_result_dataframe['Coluna_B'] = ['Teste 1', 'Teste 2']

        pd_testing.assert_frame_equal(left=test_dataframe_utils.df, right=test_result_dataframe)


    def test_remove_rows_by_index(self):
        """
            Test if we can remove some indexes properly given a CSV file, 
            a file containing columns to remove  and a file containing the
            formatted columns names for the ones which were not removed.
        """
        test_dataframe_utils = DataframeUtils('./tests/df_test.csv', ';', './tests/unused_columns.txt', './tests/formatted_columns.txt')
        # the index is not important, but when we internally format df we need to reset index because we drop some not important rows
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)
        test_dataframe_utils.remove_rows_by_index([0])
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)

        test_result_dataframe = pd.DataFrame()
        test_result_dataframe['Coluna_A'] = ['2']
        test_result_dataframe['Coluna_B'] = ['Teste 2']
        test_result_dataframe['Coluna_C'] = ['101']

        pd_testing.assert_frame_equal(left=test_dataframe_utils.df, right=test_result_dataframe)


    def test_remove_value_from_df(self):
        """
            Test if we can remove some rows according to a condition in one column 
            given a CSV file, a file containing columns to remove  and a file 
            containing the formatted columns names for the ones which were not removed.
        """
        test_dataframe_utils = DataframeUtils('./tests/df_test.csv', ';', './tests/unused_columns.txt', './tests/formatted_columns.txt')
        # the index is not important, but when we internally format df we need to reset index because we drop some not important rows
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)
        test_dataframe_utils.remove_value_from_df('Teste 2', 'Coluna_B')
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)

        test_result_dataframe = pd.DataFrame()
        test_result_dataframe['Coluna_A'] = ['1']
        test_result_dataframe['Coluna_B'] = ['Teste 1']
        test_result_dataframe['Coluna_C'] = ['100']
        
        pd_testing.assert_frame_equal(left=test_dataframe_utils.df, right=test_result_dataframe)


    def test_replace_list_values_by_condition_eq(self):
        """
            Test if we can replace a list of values from a column for 
            a new value consideting an equality condition
            given a CSV file, a file containing columns to remove  and a file 
            containing the formatted columns names for the ones which were not removed.
        """
        test_dataframe_utils = DataframeUtils('./tests/df_test.csv', ';', './tests/unused_columns.txt', './tests/formatted_columns.txt')
        # the index is not important, but when we internally format df we need to reset index because we drop some not important rows
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)
        test_dataframe_utils.replace_list_values_by_condition('Coluna_B', ['Teste 1', 'Teste 2'], 'Teste', 'eq')

        test_result_dataframe = pd.DataFrame()
        test_result_dataframe['Coluna_A'] = ['1', '2']
        test_result_dataframe['Coluna_B'] = ['Teste', 'Teste']
        test_result_dataframe['Coluna_C'] = ['100', '101']
        
        pd_testing.assert_frame_equal(left=test_dataframe_utils.df, right=test_result_dataframe)


    def test_replace_list_values_by_condition_diff(self):
        """
            Test if we can replace a list of values from a column for 
            a new value consideting a difference condition
            given a CSV file, a file containing columns to remove  and a file 
            containing the formatted columns names for the ones which were not removed.
        """
        test_dataframe_utils = DataframeUtils('./tests/df_test.csv', ';', './tests/unused_columns.txt', './tests/formatted_columns.txt')
        # the index is not important, but when we internally format df we need to reset index because we drop some not important rows
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)
        test_dataframe_utils.replace_list_values_by_condition('Coluna_B', ['Teste 2'], 'Teste 2', 'diff')

        test_result_dataframe = pd.DataFrame()
        test_result_dataframe['Coluna_A'] = ['1', '2']
        test_result_dataframe['Coluna_B'] = ['Teste 2', 'Teste 2']
        test_result_dataframe['Coluna_C'] = ['100', '101']
        
        pd_testing.assert_frame_equal(left=test_dataframe_utils.df, right=test_result_dataframe)
    

    def test_replace_list_values_by_condition_gt(self):
        """
            Test if we can replace a list of values from a column for 
            a new value consideting a 'greater than' condition
            given a CSV file, a file containing columns to remove  and a file 
            containing the formatted columns names for the ones which were not removed.
        """
        test_dataframe_utils = DataframeUtils('./tests/df_test.csv', ';', './tests/unused_columns.txt', './tests/formatted_columns.txt')
        # the index is not important, but when we internally format df we need to reset index because we drop some not important rows
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)
        test_dataframe_utils.replace_list_values_by_condition('Coluna_A', ['1'], '0', 'gt')

        test_result_dataframe = pd.DataFrame()
        test_result_dataframe['Coluna_A'] = ['1', '0']
        test_result_dataframe['Coluna_B'] = ['Teste 1', 'Teste 2']
        test_result_dataframe['Coluna_C'] = ['100', '101']
        
        pd_testing.assert_frame_equal(left=test_dataframe_utils.df, right=test_result_dataframe)


    def test_replace_list_values_by_condition_geq(self):
        """
            Test if we can replace a list of values from a column for 
            a new value consideting a 'greater than or equal' condition
            given a CSV file, a file containing columns to remove  and a file 
            containing the formatted columns names for the ones which were not removed.
        """
        test_dataframe_utils = DataframeUtils('./tests/df_test.csv', ';', './tests/unused_columns.txt', './tests/formatted_columns.txt')
        # the index is not important, but when we internally format df we need to reset index because we drop some not important rows
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)
        test_dataframe_utils.replace_list_values_by_condition('Coluna_C', ['101'], '1000', 'geq')

        test_result_dataframe = pd.DataFrame()
        test_result_dataframe['Coluna_A'] = ['1', '2']
        test_result_dataframe['Coluna_B'] = ['Teste 1', 'Teste 2']
        test_result_dataframe['Coluna_C'] = ['100', '1000']
        
        pd_testing.assert_frame_equal(left=test_dataframe_utils.df, right=test_result_dataframe)


    def test_replace_list_values_by_condition_lt(self):
        """
            Test if we can replace a list of values from a column for 
            a new value consideting a 'lower than' condition
            given a CSV file, a file containing columns to remove  and a file 
            containing the formatted columns names for the ones which were not removed.
        """
        test_dataframe_utils = DataframeUtils('./tests/df_test.csv', ';', './tests/unused_columns.txt', './tests/formatted_columns.txt')
        # the index is not important, but when we internally format df we need to reset index because we drop some not important rows
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)
        test_dataframe_utils.replace_list_values_by_condition('Coluna_A', ['2'], '0', 'lt')

        test_result_dataframe = pd.DataFrame()
        test_result_dataframe['Coluna_A'] = ['0', '2']
        test_result_dataframe['Coluna_B'] = ['Teste 1', 'Teste 2']
        test_result_dataframe['Coluna_C'] = ['100', '101']
        
        pd_testing.assert_frame_equal(left=test_dataframe_utils.df, right=test_result_dataframe)


    def test_replace_list_values_by_condition_leq(self):
        """
            Test if we can replace a list of values from a column for 
            a new value consideting a 'lower than or equal' condition
            given a CSV file, a file containing columns to remove  and a file 
            containing the formatted columns names for the ones which were not removed.
        """
        test_dataframe_utils = DataframeUtils('./tests/df_test.csv', ';', './tests/unused_columns.txt', './tests/formatted_columns.txt')
        # the index is not important, but when we internally format df we need to reset index because we drop some not important rows
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)
        test_dataframe_utils.replace_list_values_by_condition('Coluna_C', ['100'], '1', 'leq')

        test_result_dataframe = pd.DataFrame()
        test_result_dataframe['Coluna_A'] = ['1', '2']
        test_result_dataframe['Coluna_B'] = ['Teste 1', 'Teste 2']
        test_result_dataframe['Coluna_C'] = ['1', '101']
        
        pd_testing.assert_frame_equal(left=test_dataframe_utils.df, right=test_result_dataframe)


    def test_replace_list_values_by_condition_unknown(self):
        """
            Test if we can replace a list of values from a column for 
            a new value consideting an unknown condition
            given a CSV file, a file containing columns to remove  and a file 
            containing the formatted columns names for the ones which were not removed.
        """
        test_dataframe_utils = DataframeUtils('./tests/df_test.csv', ';', './tests/unused_columns.txt', './tests/formatted_columns.txt')
        # the index is not important, but when we internally format df we need to reset index because we drop some not important rows
        test_dataframe_utils.df = test_dataframe_utils.df.reset_index(drop=True)
        test_dataframe_utils.replace_list_values_by_condition('Coluna_B', ['Teste 2'], 'Teste 200', 'dumb')

        test_result_dataframe = pd.DataFrame()
        test_result_dataframe['Coluna_A'] = ['1', '2']
        test_result_dataframe['Coluna_B'] = ['Teste 1', 'Teste 2']
        test_result_dataframe['Coluna_C'] = ['100', '101']
        
        pd_testing.assert_frame_equal(left=test_dataframe_utils.df, right=test_result_dataframe)
