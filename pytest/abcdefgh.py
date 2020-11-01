import pytest
from demo import find_min, helper
import pdb

# we want to create a method to find the minimum value of a list
# the method's name: find_min


@pytest.mark.parametrize(
    "arr, expected",
    [ 
        ([2,3,10], 2),
        ([1001], 1001),
        ([], None)
    ]
)
def test_min(arr, expected):
    assert find_min(arr) == expected

def test_find_min_error(capsys):
    # if the inout is None, then find_min should print an arror message
    find_min(None)
    out, err = capsys.readouterr()
    assert err == "fatal error: input array should not be none\n"

def test_helper(capsys):
    # capsys: capturing the stdout/stderr from sys
    helper()
    out, err = capsys.readouterr()
    assert "find_min(arr): it's a  function to find out the minimal number in an array\n" == out