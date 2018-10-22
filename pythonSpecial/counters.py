from collections import Counter


def get_letter_count(input_str):
    print(Counter(input_str))


def get_word_count(input_str):
    print(Counter(input_str.split()))


def get_most_common(input_str,most_common_words_req):
    print(Counter(input_str.split()).most_common(most_common_words_req))


def get_count():
    string_to_test = "hello world, this is a test for testing test cases for counter"
    most_common_words_req = 2
    # Case 1 - get Count of letters
    get_letter_count(string_to_test)
    # Case 2 - get Count of Words
    get_word_count(string_to_test)
    # Case 3 - Most Common word in the sentence
    get_most_common(string_to_test,most_common_words_req)


def main_counter():
    get_count()
