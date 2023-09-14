import pytest

from twitter import Twitter


# Fixture
# @pytest.fixture(scope='function')
# def twitter():
#     twitter = Twitter()
#     return twitter

@pytest.fixture()
def prepare_backend_file():
    # instead of creating backend file in proper function we can mock it here and pass
    # to fixture_twitter, it doesn't need tear down delete later also
    with open('test.txt', 'w') as backend_file:
        pass

# @pytest.fixture(autouse=True)
# def prepare_backend_file():
#     # auto-use runs before every test and is considered as unsafe method
#     with open('test.txt', 'w') as backend_file:
#         pass


@pytest.fixture(params=[None, 'test.txt'], name='twitter')
def fixture_twitter(prepare_backend_file, request):
    twitter = Twitter(backend=request.param)
    yield twitter
    twitter.delete()


def test_initialization(twitter):
    # twitter = Twitter()
    assert twitter


def test_single_message(twitter):
    # Given
    # twitter = Twitter()
    # When
    twitter.tweet('TEST MESSAGE 1')
    # Then
    assert twitter.tweets == ['TEST MESSAGE 1']


def test_long_message(twitter):
    # here we expect both Exception (context manager works as assertion)
    # and that the list will be empty - then test passes
    # twitter = Twitter()
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
    # twitter = Twitter()
    assert twitter.find_hashtag(message) == expected
