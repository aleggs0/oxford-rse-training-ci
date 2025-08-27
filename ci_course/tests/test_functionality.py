import pytest
import ci_course


def test_greet():
    """
    Test the function `greet` in functionality.py
    """
    assert ci_course.greet() == "Hello "
    assert ci_course.greet("Fergus") == "Hello Fergus"

@pytest.mark.parametrize(
    "input_args    , expected_min",
    [
        ((1, 2, 3), 1),
        ((1.2, 2.3), 1.2),
        ((-1.2, -3), -3),
        ((), None),
        (("eggs", "spam"), None),
        (("eggs", 9, "spam"), 9),
    ])
def test_minimum(input_args, expected_min):
    """
    Test the function `minimum` in functionality.py
    """
    result = ci_course.minimum(*input_args)
    if expected_min is None:
        assert result is None
    else:
        assert result == expected_min
