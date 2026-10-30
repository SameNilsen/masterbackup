def test_all_lower_keys_returns_true():
    assert check_dict_case({"a": 1, "b": 2, "c3": 3}) is True


def test_all_upper_keys_returns_true():
    assert check_dict_case({"A": 1, "B": 2, "C3": 3}) is True


def test_mixed_case_keys_returns_false():
    assert check_dict_case({"a": 1, "B": 2, "c": 3}) is False


def test_non_string_key_returns_false():
    assert check_dict_case({8: "apple", "a": 2}) is False


def test_empty_dict_returns_false():
    assert check_dict_case({}) is False


def test_empty_string_key_returns_false():
    assert check_dict_case({"": 1, "b": 2}) is False

def check_dict_case(d):
    if not d:
        return False
    lower_count = 0
    upper_count = 0
    for key in d:
        if not isinstance(key, str):
            return False
        if key == '':
            return False
        if key.islower():
            lower_count += 1
        elif key.isupper():
            upper_count += 1
        else:
            return False
    return (lower_count > 0 and upper_count == 0) or (upper_count > 0 and lower_count == 0)

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

