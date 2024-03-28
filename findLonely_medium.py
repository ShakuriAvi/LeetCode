'''

2150.Find All Lonely Numbers in the Array

Array
Medium
https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/description/

Acceptance Rate
60.2% Submissions
67.5K Accepted
40.7K

runtime:97% memory:20%
'''

from typing import List
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        temp_number,res = dict(),[]
        for num in nums:
            if num in temp_number:
                temp_number[num] += 1
            else:
                temp_number[num] = 1
        for num in nums:
            if temp_number[num] > 1 or num+1 in temp_number  or num-1 in temp_number:
                continue
            else:
                res.append(num)
        return res


'''
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        dic={}
        res=[]
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in nums:
            if dic[i]==1:
                if (i-1 not in dic) and (i+1 not in dic):
                    res.append(i)
        return res
'''

