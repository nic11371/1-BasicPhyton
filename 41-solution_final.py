from typing import List


class Twitter:
    def __init__(self):
        self.feed = []
        self.post_dict = {}
        self.followers_dict = {}

    def post_tweet(self, user_id, tweet_id):
        if user_id in self.post_dict:
            k = self.post_dict[user_id]
            k.append(tweet_id)
        else:
            self.post_dict[user_id] = [tweet_id]
        return sorted(self.post_dict)

    def get_news_feed(self, user_id) -> List[int]:
        current = []
        for k in self.post_dict:
            if k in self.followers_dict[user_id]:
                current.append(self.post_dict[k])
                self.feed = [x for y in current for x in y]
                self.feed.reverse()
        return self.feed[0:10]

    def follow(self, follower_id, followee_id):
        if follower_id in self.followers_dict:
            f = self.followers_dict[follower_id]
            f.append(followee_id)
        else:
            self.followers_dict[follower_id] = [followee_id]
        return self.followers_dict

    def unfollow(self, follower_id, followee_id):
        if followee_id in self.followers_dict[follower_id]:
            self.followers_dict[follower_id].remove(followee_id)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# twitter = Twitter()
# twitter.follow(1, 2)
# twitter.follow(1, 3)
# twitter.post_tweet(2, 4)
# twitter.post_tweet(2, 6)
# twitter.post_tweet(3, 2)
# twitter.post_tweet(3, 7)
# twitter.post_tweet(3, 3)
# twitter.post_tweet(3, 8)
# twitter.post_tweet(2, 1)
# twitter.post_tweet(2, 9)
# twitter.follow(1, 4)
# twitter.post_tweet(4, 5)
# twitter.post_tweet(4, 10)
# twitter.unfollow(1, 2)
# twitter.post_tweet(5, 11)
# twitter.post_tweet(5, 12)
# twitter.post_tweet(5, 13)
# twitter.post_tweet(6, 14)
# twitter.follow(1, 5)
# twitter.post_tweet(7, 15)
# twitter.post_tweet(7, 16)
# twitter.post_tweet(7, 17)
# twitter.post_tweet(7, 18)
# twitter.follow(1, 7)
# print(twitter.get_news_feed(1))
# print(twitter.post_dict)
# print(twitter.followers_dict)
