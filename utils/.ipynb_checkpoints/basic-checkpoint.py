"""
Utilities functions.

This module aims to concentrate some utilities functions.

Author: Antonio Pedro Santos Alves
Advisor: Marcos Kalinowski
"""

def rename_values(*, rename_mapping: dict, values: list[any], not_found_value: str = '') -> list[any]:
    """
        Rename values from a list according to a dict 
        with new values labels
    """
    renamed_values = []
    
    for value in values:
        renamed_values.append(rename_mapping.get(value, not_found_value if not_found_value else value))
    
    return renamed_values


def format_wordcloud_text(*, texts: list[str], use_sep: bool) -> dict:
    """
        Build a dict with a word and its importance/weight 
        in the corpus.
    """
    weighted_text = {}
    for text in texts:
        # split the text by a separator, limited to a whitespace
        if use_sep:
            splitted_text = text.split(" ")
            for split in splitted_text:
                if weighted_text.get(split):
                    weighted_text[split] = weighted_text[split] + 1
                else:
                    weighted_text[split] = 1
        else:
            if weighted_text.get(text):
                weighted_text[text] = weighted_text[text] + 1
            else:
                weighted_text[text] = 1
                
    return weighted_text
