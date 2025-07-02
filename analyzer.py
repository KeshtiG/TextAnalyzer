#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ANALYZER FUNCTIONS
"""

import os
import string
from operator import itemgetter

def change_file(user_input):
    """
    Change text file
    """
    folder = "texts"
    filename = "phil.txt"
    if user_input:
        filename = user_input
    filepath = os.path.join(folder, filename)
    return filepath


def count_lines(filepath):
    """
    Count lines
    """

    with open(filepath, "r", encoding="utf-8") as file_desc:

        line_count = 0

        for line in file_desc:
            # Line is counted if not empty after strip
            if line.strip():
                line_count += 1

    return line_count


def count_words(filepath):
    """
    Count words
    """

    with open(filepath, "r", encoding="utf-8") as file_desc:

        word_count = 0

        for line in file_desc:
            # Split line into words
            words = line.split()
            # Add to word_count for every word in line
            word_count += len(words)

    return word_count


def count_letters(filepath):
    """
    Count letters
    """

    with open(filepath, "r", encoding="utf-8") as file_desc:

        letter_count = 0

        for line in file_desc:
            # Strip line from any trailing whitespaces
            line = line.rstrip()
            # Remove punctuations and make lower
            line = remove_punct_make_lower(line)
            # Check if char is a letter and count it
            for char in line:
                if char.isalpha():
                    letter_count += 1

    return letter_count


def count_frequency(filepath, input_item):
    """
    Count word or letter frequency
    """

    frequency_dict = {}

    with open(filepath, "r", encoding="utf-8") as file_desc:
        for line in file_desc:
            # Remove punctuations and convert to lower case
            line = remove_punct_make_lower(line)

            if input_item == "words":
                # Split line into words
                for word in line.split():
                    # Updates word frequency in dictionary
                    frequency_dict[word] = frequency_dict.get(word, 0) + 1

            elif input_item == "letters":
                # Iterate over each letter
                for letter in line:
                    if letter.isalpha():
                        # Update letter frequency in dictionary
                        frequency_dict[letter] = frequency_dict.get(letter, 0) + 1

    # Convert dictionary to list
    frequency_list = list(frequency_dict.items())

    # Sort by frequency (index 1) then alphabetically (index 0)
    frequency_sorted = sorted(frequency_list, key=itemgetter(1, 0), reverse=True)

    # Fetch sum of words/letters
    input_item_sum = 0
    if input_item == "words":
        input_item_sum = count_words(filepath)
    elif input_item == "letters":
        input_item_sum = count_letters(filepath)

    input_item_str = ""
    # Fetch the top 8 words/letters, calculate percentage and add to string
    for item, freq in frequency_sorted[:8]:
        percentage = round((freq / input_item_sum * 100), 1)
        input_item_str += f"{item:<12} {freq:>3}, {percentage:>4}%\n"

    # Return string without the last newline
    return input_item_str.strip()


def remove_punct_make_lower(line):
    """
    Remove punctuations and make lower
    """
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.lower()

    return line


def get_all_results(filepath):
    """
    Get all results
    """
    # Call functions to get results
    line_count = count_lines(filepath)
    word_count = count_words(filepath)
    letter_count = count_letters(filepath)
    word_freq = count_frequency(filepath, "words")
    letter_freq = count_frequency(filepath, "letters")

    # Store results and headings in variable
    result = (
        f"Lines: {line_count}\n"
        f"Words: {word_count}\n"
        f"Letters: {letter_count}\n\n"
        f"Word Frequency:\n{word_freq}\n\n"
        f"Letter Frequency:\n{letter_freq}"
    )

    return result
