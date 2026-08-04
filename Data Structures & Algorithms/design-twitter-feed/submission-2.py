class Twitter:

    def __init__(self):
        self.t = 0
        self.following_map = {}
        self.tweets_map = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_map:
            self.tweets_map[userId] = []
        
        self.tweets_map[userId].append((self.t, tweetId))
        self.t -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following_map:
            self.following_map[userId] = set()
        self.following_map[userId].add(userId)

        minHeap = []
        res = []

        for followee in self.following_map[userId]:
            if followee in self.tweets_map:
                idx = len(self.tweets_map[followee]) - 1
                count, tweetId = self.tweets_map[followee][idx]
                heapq.heappush(minHeap, [count, tweetId, followee, idx-1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweets_map[followeeId][idx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, idx-1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following_map:
            self.following_map[followerId] = set()
        
        self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following_map:
            return
        
        if followeeId not in self.following_map[followerId]:
            return

        self.following_map[followerId].remove(followeeId)
