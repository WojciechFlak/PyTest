import pytest

from twitter import Twitter


def test_initialization():
    twitter = Twitter()
    assert twitter


def test_single_message():
    # Given
    twitter = Twitter()
    # When
    twitter.tweet('TEST MESSAGE 1')
    # Then
    assert twitter.tweets == ['TEST MESSAGE 1']


def test_long_message():
    # here we expect both Exception (context manager works as assertion)
    # and that the list will be empty - then test passes
    twitter = Twitter()
    with pytest.raises(Exception):
        twitter.tweet('test'*41)
    assert twitter.tweets == []
