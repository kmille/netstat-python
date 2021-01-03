#!/usr/bin/env python3
import sys
import pytest

"""
useful command line arguments:
    - more verbose: -v
    - show stdout/prints of test_functions: -s
    - run python debugger (pdb) if erros exists: --pdb
    - run only tests containing 'network': -k network
    - run all tests except ones having 'network' in the name: -k 'not network'
"""


def test_example():
    print(f"this will only work on python3 {4+4}")
    assert 1 == 1


def test_raise():
    with pytest.raises(AttributeError):
        i = 3
        i.upper()


@pytest.fixture
def result():
    return 4


def test_result(result):
    assert result == 4


@pytest.mark.parametrize(
    ('n', 'expected'), [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
    ]
)
def test_increment(n, expected):
    assert n + 1 == expected


# combine fixture with parameterize
@pytest.mark.parametrize(('number1', 'number2'), [(1, 3), (2, 2)])
def test_calc_add(result, number1, number2):
    assert result == number1 + number2


def test_tmpdir_file(tmpdir_factory):
    # https://docs.pytest.org/en/stable/tmpdir.html
    # creates them in /tmp/pytest-of-kmille/pytest-{0-2,current}
    # removes anything older than that
    tmp = tmpdir_factory.mktemp("data")
    print(f"tmp dir: {tmp}")


def is_palindrome(a):
    return a == a[::-1]


@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("bob", True),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result


@pytest.mark.xfail
def test_wrong():
    assert 2 == 2


@pytest.mark.xfail
def test_wrong2():
    assert 1 == 2


#def test_wrong2():
#    if 1 == 2:
#        pytest.xfail("no right")


@pytest.mark.skip(reason="no way of currently testing this")
def test_not_now():
    assert 1 == 2


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
def test_skip_here():
    assert 1 == 1



