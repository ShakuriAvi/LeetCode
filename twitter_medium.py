'''
01\11\23
355. Design Twitter

Hash Map
Medium
https://leetcode.com/problems/design-twitter/description/

"Acceptance Rate
38.6%. Submissions
384.3K .Accepted
148.3K"

'''


class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Twitter(object):
    def __init__(self):
        self.followers = dict()
        self.users_posts = LinkedList({"user_id": "head", "tweet_id": -1})

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        head = self.users_posts
        sec_node = head.next
        user_post = {"user_id": userId, "tweet_id": tweetId}
        new_node = LinkedList(user_post)
        head.next = new_node
        new_node.next = sec_node
        self.follow(userId, userId)

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        posts = []
        head = self.users_posts
        node = head.next
        while node:
            print(node.val["user_id"], self.followers)
            if node.val["user_id"] in self.followers[userId]:
                posts.append(node.val["tweet_id"])
            node = node.next
        return posts[0:10]

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.followers:
            self.followers[followerId] = dict()

        self.followers[followerId][followeeId] = True

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                del self.followers[followerId][followeeId]

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


'''
"class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = []
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        i=len(self.tweets)-1
        while i>=0 and len(res)<10:
            if self.tweets[i][0] in self.users[userId] or self.tweets[i][0]==userId:
                res.append(self.tweets[i][1])
            i-=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]: self.users[followerId].remove(followeeId)"

'''
