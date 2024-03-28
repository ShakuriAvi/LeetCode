'''
13\02\24

2829. Determine the Minimum Sum of a k-avoiding Array

Greedy

Medium

https://leetcode.com/problems/binary-search-tree-iterator/description/

"Accepted
32.5K
Submissions
53.5K
Acceptance Rate
60.8%"


"runtime Beats
58.62%
of users with Python, memory Beats
89.66%
of users with Python"


'''

class Solution(object):


    def minimumSum(self, n, k):
        res = 0
        i = 1
        cache = set()
        end = n + 1
        while end > i:
            if k - i in cache:
                end += 1
                i += 1
                continue
            res += i
            cache.add(i)
            i += 1
        return res



'''
"class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        hashSet, curNum, curSum = set(), 1, 0
        while len(hashSet) < n:
            if k - curNum not in hashSet:
                hashSet.add(curNum)
                curSum += curNum
            curNum += 1
        return sum(hashSet)"

'''