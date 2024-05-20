"""
Easy dataframe handler.

This module aims to facilitate some basics dataframe operations 
that sometimes imply in some extra cells, lines of codes 
and google searches. 

Author: Antonio Pedro Santos Alves
Advisor: Marcos Kalinowski
"""

import pandas as pd
from statistics import mean, median


class DataframeUtils:    
    def __init__(self, df_path: str, sep: str, to_discard_columns_file: str, to_format_columns_file: str):
        self.to_discard_columns_file = to_discard_columns_file
        self.to_format_columns_file = to_format_columns_file
        self.df = self.get_df(df_path, sep)
        self.format_df()
      

    def list_columns(self):
        """
            List columns from dataframe with two auxiliar identifiers
            in order to allow user to see any unexpected whitespace on
            column name.
        """
        for column in list(self.df.columns):
            print(">" + column + "<")


    def remove_columns(self, columns: list[str]):
        """
            Remove some columns from dataframe according to 'columns' 
            and update it.
        """
        self.df = self.df.drop(columns=columns)


    def remove_rows_by_index(self, indexes: list[int]):
        """
            Remove some rows from dataframe according to 'indexes' 
            and update it.
        """
        self.df = self.df.drop(indexes)


    def remove_value_from_df(self, value: str, column: str):
        """
            Remove all rows that contains a specific value in one column
        """
        self.df.drop( self.df.loc[ self.df[column] == value].index, inplace=True ) 


    def replace_value_by_condition(self, column: str, old_value: any, new_value: any, condition: str):
        """
            Replace value in a specific column according to one of the specified
            conditions over current value, such as equality, difference and greater
            operators, and update current dataframe.

            In case of undefined condition, we preserve dataframe
        """
        if condition == 'eq':
            self.df.loc[self.df[column] == old_value, column] = new_value

        elif condition == 'gt':
            self.df.loc[self.df[column] > old_value, column] = new_value

        elif condition == 'lt':
            self.df.loc[self.df[column] < old_value, column] = new_value

        elif condition == 'geq':
            self.df.loc[self.df[column] >= old_value, column] = new_value

        elif condition == 'leq':
            self.df.loc[self.df[column] <= old_value, column] = new_value

        elif condition == 'diff':
            self.df.loc[self.df[column] != old_value, column] = new_value
        
        else:
            self.df = self.df


    def replace_list_values_by_condition(self, column: str, old_values: list[any], new_value: any, condition: str):
        """
            Replace a list of values in a specific column according to one of the specified
            conditions over current values, such as equality, difference and greater
            operators, and update current dataframe.

            In case of undefined condition, we preserve dataframe
        """
        for value in old_values:
            self.replace_value_by_condition(column, value, new_value, condition)


    def format_df(self):
        """
            Format dataframe columns discarding those which are specified
            in 'discard_columns_path' and setting the column name of
            remaining columns according to what is specified in
            'formatted_columns_path'.

            It is important to notice that the order of columns in
            'formatted_columns_path' must follow the same order of
            dataframe columns without the removed columns.
        """
    
        with open(self.to_discard_columns_file, encoding="utf-8") as file_unused_columns:
            unused_columns = file_unused_columns.readlines()

        # remove '\n' character
        unused_columns = [unused_column.replace("\n", '') for unused_column in unused_columns]

        self.remove_columns(unused_columns)

        # remove the first two rows - unnecessary data describing the columns
        self.remove_rows_by_index([0, 1])

        with open(self.to_format_columns_file, encoding="utf-8") as file_formatted_columns:
            formatted_columns = file_formatted_columns.readlines()
            
        # remove '\n' character
        formatted_columns = [formatted_column.replace("\n", '') for formatted_column in formatted_columns]
        
        self.df.columns = formatted_columns


    def get_df(self, df_path: str, sep: str) -> pd.DataFrame:
        """
            Read dataframe and format it according to some external files
        """
        df = pd.read_csv(df_path, sep=sep)

        return df
