import pytest



"""
Each attribute or response that I take from witness needs to be check under testing mechanism which are demonstrated below.
So for string, the input must be in the form of str or just string/text/message/word and so on.
Furthermore, every single sureness score must be checked as well and raise TypeError or ValueError based on the form of that input.
Every single sureness score must be a natural number between 0 and 100 and takes no character or word, just a raw natural integer.
The testing was done by using pytest library to parametrize all possible inputs from witnesses.
"""

# 1. SCORES VALIDATION & TESTS

def errors_for_invalid_scores(score):
    """Validates sureness scores (must be int/float between 0 and 100)."""
    if not isinstance(score, (int, float)) or isinstance(score, bool):
        raise TypeError("Every number must be Integer or Float")
    if not (0 <= score <= 100):
        raise ValueError("Every score must be in the range between 0 and 100")
    
    return f"{score} is accepted"


@pytest.mark.parametrize("invalid_score, expected_error", [
    (-1, ValueError),
    (110, ValueError),
    (None, TypeError),
    ("80", TypeError),
    ("hello", TypeError),
]) 
def test_errors_for_scores(invalid_score, expected_error):
    with pytest.raises(expected_error):
        errors_for_invalid_scores(invalid_score)


@pytest.mark.parametrize("valid_score", [0, 50, 70, 100])
def test_valid_scores(valid_score):
    assert "is accepted" in errors_for_invalid_scores(valid_score)



# 2. YES / NO / IDK VALIDATION & TESTS


def errors_for_yes_or_no(string):
    """Validates yes/no/idk questions."""
    if not isinstance(string, str):
        raise TypeError("Your text must be in the form of str")
    if string == "":
        raise ValueError("Strings cannot be empty")
    if string not in ["yes", "no", "idk"]:
        raise ValueError("Every yes or no question must be in the form of either (yes/no/idk)")
    
    return f"{string} is accepted"


@pytest.mark.parametrize("invalid_string, expected_error", [
    ("yes1", ValueError),
    ("yesssss", ValueError),
    ("Yes", ValueError),
    ("YES", ValueError),
    ("Y", ValueError),
    ("y", ValueError),
    (10, TypeError),
    ("No", ValueError),
    ("NO", ValueError),
    ("NOOOO", ValueError),
    ("nooo", ValueError),
    ("no10", ValueError),
    ("10no", ValueError),
    ("maybe", ValueError),
    ("", ValueError),
]) 

def test_errors_for_strings(invalid_string, expected_error):
    with pytest.raises(expected_error):
        errors_for_yes_or_no(invalid_string)


@pytest.mark.parametrize("valid_string", ["yes", "no", "idk"])
def test_valid_strings(valid_string):
    assert "is accepted" in errors_for_yes_or_no(valid_string)



# 3. HAIR COLOUR TESTS

HAIR_COLOURS = [
    "black", 
    "brown", 
    "blonde", 
    "red", 
    "gray", 
    "white", 
    "auburn", 
    "chestnut", 
    "ginger", 
    "platinum", 
    "strawberry blonde", 
    "salt and pepper"
]

def errors_for_colours(string):
    """Validates hair color inputs."""
    if not isinstance(string, str):
        raise TypeError("Your text must be in the form of str")
    if string == "":
        raise ValueError("Strings cannot be empty")
    if string == "idk" or string in HAIR_COLOURS:
        return f"{string} is accepted"
    else:
        raise ValueError("Hair colour does not make sense")


@pytest.mark.parametrize("invalid_string, expected_error", [
    ("blonde1", ValueError),
    ("blondEEE", ValueError),
    ("10", ValueError),
    ("bdfgrgr", ValueError),
    ("Y", ValueError),
    ("y", ValueError),
    (10, TypeError),
    ("redblonde", ValueError),
    ("blondehair", ValueError),
    ("blueandyellow", ValueError),
    ("", ValueError),
]) 
def test_errors_for_colours(invalid_string, expected_error):
    with pytest.raises(expected_error):
        errors_for_colours(invalid_string)


@pytest.mark.parametrize("valid_colour", ["blonde", "black", "ginger", "idk"])

def test_valid_colours(valid_colour):
    assert "is accepted" in errors_for_colours(valid_colour)
