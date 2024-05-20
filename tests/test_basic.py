import unittest
from utils.basic import rename_values, format_wordcloud_text

class TestBasic(unittest.TestCase):
    def test_rename_values_all_mapped_values(self):
        """
            Test to check if all values in a list is being replaced
            once all list values are mapped in a rename mapping dict.
        """
        dict_rename_mapping = {'value_1' : 'Value 1', 'value_2': 'Value 2'}
        list_values = ['value_1', 'value_2']
        self.assertEqual(rename_values(rename_mapping=dict_rename_mapping, values=list_values),
         ['Value 1', 'Value 2'])


    def test_rename_values_missing_mapped_values_with_param(self):
        """
            Test to check if only some values in a list is being replaced
            by the specified param once only some list values are mapped
            in a rename mapping dict.
        """
        dict_rename_mapping = {'value_1' : 'Value 1', 'value_2': 'Value 2'}
        list_values = ['value_1', 'value_11', 'value_2', 'value_22']
        self.assertEqual(rename_values(rename_mapping=dict_rename_mapping, values=list_values, not_found_value='Not Found'),
         ['Value 1', 'Not Found', 'Value 2', 'Not Found'])


    def test_rename_values_missing_mapped_values_without_param(self):
        """
            Test to check if only some values in a list is being replaced
            by the default value once only some list values are mapped
            in a rename mapping dict and no param is specified for not found
            value.
        """
        dict_rename_mapping = {'value_1' : 'Value 1', 'value_2': 'Value 2'}
        list_values = ['value_1', 'value_11', 'value_2', 'value_22']
        self.assertEqual(rename_values(rename_mapping=dict_rename_mapping, values=list_values),
         ['Value 1', 'value_11', 'Value 2', 'value_22'])


    def test_format_wordcloud_text_with_sep(self):
        """
            Test to check wordcloud text dictionary
            when the text is being separated by whitespace.

            In this case, words like 'Human Resources' are counted
            as 'Human' and 'Resources' separatedely.
        """
        list_words = ['Human Resources', 'Human', 'Resources']
        self.assertEqual(format_wordcloud_text(texts=list_words, use_sep=True),
         {'Human': 2, 'Resources': 2})


    def test_format_wordcloud_text_without_sep(self):
        """
            Test to check wordcloud text dictionary
            when the text is being separated by whitespace.

            In this case, words like 'Human Resources' are counted
            as 'Human Resources', together.
        """
        list_words = ['Human Resources', 'Human', 'Resources', 'Human']
        self.assertEqual(format_wordcloud_text(texts=list_words, use_sep=False),
         {'Human Resources': 1, 'Human': 2, 'Resources': 1})
