import pytest
import requests

from twitter import Twitter


class ResponseGetMock(object):
    @staticmethod
    def json():
        return {'avatar_url': 'test'}


# Fixture
# @pytest.fixture(scope='function')
# def twitter():
#     twitter = Twitter()
#     return twitter

@pytest.fixture()
def prepare_backend_file(tmpdir):
    temp_file = tmpdir.join('test.txt')
    temp_file.write('')
    return temp_file


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr('requests.sessions.Session.request')


# @pytest.fixture(autouse=True)
# def prepare_backend_file():
#     # auto-use runs before every test and is considered as unsafe method
#     with open('test.txt', 'w') as backend_file:
#         pass

@pytest.fixture(params=[None, 'python'])
def username(request):
    return request.param


@pytest.fixture(params=['list', 'prepare_backend_file'], name='twitter')
def fixture_twitter(prepare_backend_file, username, request, monkeypatch):
    if request.param == 'list':
        twitter = Twitter(username=username)
    elif request.param == 'prepare_backend_file':
        twitter = Twitter(backend=prepare_backend_file, username=username)

    def monkey_return(url):
        return ResponseGetMock()

    monkeypatch.setattr(requests, 'get', monkey_return)
    return twitter


def test_initialization(twitter):
    # twitter = Twitter()
    assert twitter


def test_single_message(twitter):
    # Given
    # twitter = Twitter()
    # When
    twitter.tweet('TEST MESSAGE 1')
    # Then
    assert twitter.tweet_messages == ['TEST MESSAGE 1']


def test_long_message(twitter):
    # here we expect both Exception (context manager works as assertion)
    # and that the list will be empty - then test passes
    # twitter = Twitter()
    with pytest.raises(Exception):
        twitter.tweet('test'*41)
    assert twitter.tweet_messages == []


def test_tweet_with_hashtag(twitter):
    assert 'the' in twitter.find_hashtag('This is #the first message wish hashtag')


def test_initialize_two_twitter_classes(prepare_backend_file):
    twitter1 = Twitter(backend=prepare_backend_file)
    twitter2 = Twitter(backend=prepare_backend_file)

    twitter1.tweet('Test message1')
    twitter2.tweet('Test message2')

    assert twitter2.tweet_messages == ['Test message1', 'Test message2']


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


def test_tweet_with_username(twitter):
    if not twitter.username:
        pytest.skip()
    twitter.tweet('Test message')
    assert twitter.tweets == [{'message': 'Test message', 'avatar': 'test'}]
