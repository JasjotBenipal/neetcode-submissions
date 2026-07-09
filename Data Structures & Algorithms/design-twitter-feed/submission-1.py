class Twitter:

    def __init__(self):
        self.time = 0
        self.followList = defaultdict(set) # userid to set of userid
        self.tweetTimes = defaultdict(list) #userid to list(time, tweetid)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetTimes[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []

        self.follow(userId, userId)

        for followers in self.followList[userId]:
            if followers in self.tweetTimes:
                index = len(self.tweetTimes[followers]) - 1
                time, tweetid = self.tweetTimes[followers][index]
                heapq.heappush(maxHeap, [time, tweetid, followers, index])
        
        while maxHeap and len(res) < 10:
            time, tweetid, followers, index = heapq.heappop(maxHeap)

            res.append(tweetid)

            index -= 1
            if index >= 0:
                time, tweetid = self.tweetTimes[followers][index]
                heapq.heappush(maxHeap, [time, tweetid, followers, index])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)
