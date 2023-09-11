import unittest

from twitter import Twitter

# unittest requires constructing test class as presented below
class TestTwitter(unittest.TestCase):

    # setUp method is called before every unit test but there is also possibility to call class for each Given
    def setUp(self):
        self.twitter = Twitter()

    def test_initialization(self):
        self.assertTrue(self.twitter)

    def test_tweet_single(self):
        # Given
        # twitter = Twitter()
        # When
        self.twitter.tweet('Test message 1')
        # Then
        self.assertEqual(self.twitter.tweets, ['Test message 2'])


if __name__ == '__main__':
    unittest.main()
