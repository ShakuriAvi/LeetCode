'''
01\07\24
355. Design Twitter
https://leetcode.com/problems/design-twitter/description/

Accepted
185K
Submissions
463.5K
Acceptance Rate
39.9%

Memory
16.59
MB
Beats
92.36%

Runtime
39
ms
Beats
31.30%

'''


from typing import List

class ListNode:
    def __init__(self, user_id: int, tweet_id: int, next=None):
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.next = next


class Twitter:

    def __init__(self):
        self.follower_by_user_id = dict()
        self.head = None



    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        new_node = ListNode(userId, tweetId, next=self.head)
        self.head = new_node



    def getNewsFeed(self, userId: int) -> List[int]:
        node = self.head
        counter = 0
        res = []
        users = self.follower_by_user_id.get(userId, set())
        while node and counter < 10:
            if node.user_id in users:
                res.append(node.tweet_id)
                counter += 1
            node = node.next
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower_by_user_id:
            self.follower_by_user_id[followerId] = set()
        self.follower_by_user_id[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        users = self.follower_by_user_id.get(followerId)
        if followeeId in users:
            users.remove(followeeId)



if __name__ == "__main__":

    # Your Twitter object will be instantiated and called as such:
    # obj = Twitter()
    # obj.postTweet(1, 5)
    # print(obj.getNewsFeed(1))
    # obj.follow(1,2)
    # obj.postTweet(2, 6)
    # print(obj.getNewsFeed(1))
    # obj.unfollow(1, 2)
    # print(obj.getNewsFeed(1))

    obj = Twitter()
    obj.postTweet(1, 5)
    obj.postTweet(1, 3)
    obj.postTweet(1, 101)
    obj.postTweet(1, 10)
    obj.postTweet(1, 2)
    obj.postTweet(1, 94)
    obj.postTweet(1, 505)
    obj.postTweet(1, 333)
    obj.postTweet(1, 22)
    obj.postTweet(1, 11)
    print(obj.getNewsFeed(1))


["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed"]
[[],[1,5],[1,3],[1,101],[1,13],[1,10],[1,2],[1,94],[1,505],[1,333],[1,22],[1,11],[1]]
'''
355. Design Twitter
Solved
Medium
Topics
Companies
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, 
and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
Each item in the news feed must be posted by users who the user followed or by the user themself.
Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.


'''