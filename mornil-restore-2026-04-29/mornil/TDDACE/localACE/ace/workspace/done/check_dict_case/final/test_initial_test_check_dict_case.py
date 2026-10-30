from solution import check_dict_case


def test_empty_dict_returns_false():
    assert not check_dict_case({})


def test_all_lowercase_dict_returns_true():
    d = {"a": 1, "b": 2, "c": 3}
    assert check_dict_case(d)


def test_all_uppercase_dict_returns_true():
    d = {"A": 1, "B": 2, "C": 3}
    assert check_dict_case(d)


def test_mixed_case_dict_returns_false():
    d = {"a": 1, "B": 2, "c": 3}
    assert not check_dict_case(d)


def test_non_string_keys_dict_returns_false():
    d = {"a": 1, 2: "two", "c": 3}
    assert not check_dict_case(d)


def test_mixed_case_with_partial_uppercase_returns_false():
    d = {"NAME": 1, "age": 2}
    assert not check_dict_case(d)

def check_dict_case(d: dict) -> bool:
    """Return True if all keys are strings of the same case (all lower or all upper).
    The result is False for an empty dictionary, for nonâstring keys, or for mixed case.
    """
    if not d:
        return False
    keys = d.keys()
    # Check type of every key
    for k in keys:
        if not isinstance(k, str):
            return False
    # Get the case of the first key
    first = next(iter(keys))
    if first.islower():
        # All must be lower
        return all(k.islower() for k in keys)
    if first.isupper():
        # All must be upper
        return all(k.isupper() for k in keys)
    return False

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

