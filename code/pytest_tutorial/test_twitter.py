import pytest

from twitter import Twitter


# Fixture
@pytest.fixture(scope='function')
def twitter():
    twitter = Twitter()
    return twitter


# @pytest.fixture
# def twitter():
#     twitter = Twitter()
#     yield twitter
#     twitter.delete()


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


def test_tweet_with_hashtag(twitter):
    assert 'the' in twitter.find_hashtag('This is #the first message wish hashtag')


# Parametrize
# Fixtures
@pytest.mark.parametrize('message, expected', (
        ('This is #the first message wish hashtag', ['the']),
        ('#This is the first message wish hashtag', ['this']),
        ('This is the first message wish #hashtag', ['hashtag']),
        ('This is the #first message wish #hashtag', ['first', 'hashtag'])
))
def test_different_hashtags(twitter, message, expected):
    twitter = Twitter()
    assert twitter.find_hashtag(message) == expected
