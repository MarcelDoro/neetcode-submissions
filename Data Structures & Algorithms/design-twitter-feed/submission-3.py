class Twitter:

    def __init__(self):
        self.users = []
        self.tweets = []
        self.follows = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users.append(userId)
        
        self.tweets.insert(0, (userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        size = 0
        result = []

        for tweet in self.tweets:
            if size == 10:
                break
            if tweet[0] == userId or (userId, tweet[0]) in self.follows:
                result.append(tweet[1])
                size += 1

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if (followerId, followeeId) not in self.follows:
            self.follows.append((followerId, followeeId))

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId, followeeId) in self.follows:
            self.follows.remove((followerId, followeeId))
