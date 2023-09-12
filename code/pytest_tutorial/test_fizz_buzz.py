import pytest

from fizz_buzz import fizz_buzz


def test_fizz():
    assert fizz_buzz(3) == 'Fizz'


def test_buzz():
    assert fizz_buzz(5) == 'Buzz'


def test_fizz_buzz():
    assert fizz_buzz(15) == 'FizzBuzz'


@pytest.mark.parametrize('input_fizzbuzz, expected',
                         [
                             (3, 'Fizz'),
                             (5, 'Buzz'),
                             (15, 'FizzBuzz'),
                             (300, 'FizzBuzz'),
                             (14, 14),
                             (147, 'Fizz'),
                             (0, 0)
                         ]
                         )
def test_fizz_buzz(input_fizzbuzz, expected):
    assert fizz_buzz(input_fizzbuzz) == expected
