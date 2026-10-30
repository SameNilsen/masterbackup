def test_check_dict_case_lowercase():
    assert check_dict_case({"a": "apple", "b": "banana"}) == True


def test_check_dict_case_uppercase():
    assert check_dict_case({"STATE": "NC", "ZIP": "12345"}) == True


def test_check_dict_case_mixed_case():
    assert check_dict_case({"a": "apple", "B": "banana"}) == False


def test_check_dict_case_non_string_key():
    assert check_dict_case({8: "banana", "a": "apple"}) == False


def test_check_dict_case_empty():
    assert check_dict_case({}) == False


def test_check_dict_case_single_lower():
    assert check_dict_case({"x": "value"}) == True


def test_check_dict_case_single_upper():
    assert check_dict_case({"X": "value"}) == True


def test_check_dict_case_upper_with_lower():
    assert check_dict_case({"CITY": "Houston", "zip": "12345"}) == False

def check_dict_case(d):
    """
    Return True if all keys of the dictionary are strings and either all lowerâcase
    or all upperâcase; return False otherwise. If the dictionary is empty return
    False.
    """
    if not d:
        return False
    # All keys must be strings
    if not all(isinstance(k, str) for k in d):
        return False
    # All lower or all upper
    return all(k.islower() for k in d) or all(k.isupper() for k in d)

def test_check():

    # Check some simple cases
    assert check_dict_case({"p":"pineapple", "b":"banana"}) == True, "First test error: " + str(check_dict_case({"p":"pineapple", "b":"banana"}))
    assert check_dict_case({"p":"pineapple", "A":"banana", "B":"banana"}) == False, "Second test error: " + str(check_dict_case({"p":"pineapple", "A":"banana", "B":"banana"}))
    assert check_dict_case({"p":"pineapple", 5:"banana", "a":"apple"}) == False, "Third test error: " + str(check_dict_case({"p":"pineapple", 5:"banana", "a":"apple"}))
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False, "Fourth test error: " + str(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
    assert check_dict_case({"STATE":"NC", "ZIP":"12345" }) == True, "Fifth test error: " + str(check_dict_case({"STATE":"NC", "ZIP":"12345" }))      
    assert check_dict_case({"fruit":"Orange", "taste":"Sweet" }) == True, "Fourth test error: " + str(check_dict_case({"fruit":"Orange", "taste":"Sweet" }))      


    # Check some edge cases that are easy to work out by hand.
    assert check_dict_case({}) == False, "1st edge test error: " + str(check_dict_case({}))

