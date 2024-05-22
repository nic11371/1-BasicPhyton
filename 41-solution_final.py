from typing import List

class Twitter:
    def __init__(self):
        self.users = []
        self.post_dict = {}
        self.followers_dict = {}

    def post_tweet(self, user_id, tweet_id):
        self.post_dict[user_id] =
        for u in user_id:
        return self.post_dict

    def follow(self, follower_id, followee_id):
        self.followers_dict[follower_id] = followee_id
        print(self.followers_dict)
        return self.followers_dict

    def unfollow(self, follower_id, followee_id):

        self.followers_dict.pop(follower_id)





twitter = Twitter()
# twitter.follow(1, 2)
# twitter.follow(1, 3)
twitter.post_tweet(2, 4)
twitter.post_tweet(2, 6)
twitter.post_tweet(3, 2)
twitter.post_tweet(3, 7)
twitter.post_tweet(3, 3)
twitter.post_tweet(3, 8)
twitter.post_tweet(2, 1)
twitter.post_tweet(2, 9)
# twitter.follow(1, 4)
twitter.post_tweet(4, 5)
twitter.post_tweet(4, 10)
# twitter.unfollow(1, 2)
twitter.post_tweet(5, 11)
twitter.post_tweet(5, 12)
twitter.post_tweet(5, 13)
twitter.post_tweet(6, 14)
# twitter.follow(1, 5)
twitter.post_tweet(7, 15)
twitter.post_tweet(7, 16)
twitter.post_tweet(7, 17)
twitter.post_tweet(7, 18)
# twitter.follow(1, 7)
# print(twitter.get_news_feed(1))
print(twitter.post_dict)