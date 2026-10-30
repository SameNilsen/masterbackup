import pytest

# Note: The target function `check_dict_case` will be provided by the code under test.

@pytest.mark.parametrize(
    "data,expected",
    [
        # 1. Empty dictionary â should be False.
        ({}, False),
        # 2. All lowerâcase keys â should be True.
        ({"a": "apple", "b": "banana"}, True),
        # 3. All upperâcase keys â should be True.
        ({"A": "alpha", "B": "beta"}, True),
        # 4. Mixed case keys â should be False.
        ({"a": "apple", "B": "banana"}, False),
        # 5. Nonâstring key â should be False.
        ({"a": "apple", 8: "banana"}, False),
        # 6. Non-string values are irrelevant; still True.
        ({"A": "alpha", "B": 123}, True),
        # 7. Mixed case with None values â still False.
        ({"Smith": None, "Brown": None}, False),
        # 8. Keys that are purely numeric strings â case not applicable, should be True.
        ({"123": "num1", "456": "num2"}, True),
    ],
)
def test_check_dict_case(data, expected):
    """Test `check_dict_case` for various dictionary key scenarios."""
    result = check_dict_case(data)
    assert result == expected
    assert isinstance(result, bool)


def check_dict_case(d):
    """Return True if all string keys are lowerâcase or upperâcase, or all keys are numeric strings.

    Parameters
    ----------
    d : dict
        Dictionary to check.

    Returns
    -------
    bool
        ``True`` if the dictionary satisfies the condition, otherwise ``False``.
    """
    # Must be a dictionary
    if not isinstance(d, dict):
        raise TypeError("Input must be a dict")

    # Empty dictionary: False
    if not d:
        return False

    # Ensure all keys are strings
    for k in d:
        if not isinstance(k, str):
            return False

    # Separate numeric-only string keys from alphabetic keys
    alpha_keys = [k for k in d if not k.isdigit()]

    # If no alphabetic keys, all numeric â treat as passing
    if not alpha_keys:
        return True

    # Check if all alphabetic keys are lower or all are upper
    if all(k.islower() for k in alpha_keys) or all(k.isupper() for k in alpha_keys):
        return True

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

