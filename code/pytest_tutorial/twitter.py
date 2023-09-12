import re


class Twitter:
    version = '1.0'

    def __init__(self):
        self.tweets = []

    def delete(self):
        print("It's the end.")

    def tweet(self, message):
        if len(message) > 160:
            raise Exception('Message too long')
        self.tweets.append(message)

    def find_hashtag(self, message):
        return [m.lower() for m in re.findall('#(\w+)', message)]
