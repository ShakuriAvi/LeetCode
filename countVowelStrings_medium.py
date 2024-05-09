'''
07\04\2024

1641. Count Sorted Vowel Strings

DP
Medium

https://leetcode.com/problems/count-sorted-vowel-strings/description/

Accepted
180.2K
Submissions
230.3K
Acceptance Rate
78.2%

Memory
166.64
MB
Beats
5.05%
of users with Python3

Runtime
4954
ms
Beats
5.05%
of users with Python3
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = ['a', 'e', 'i', 'o', 'u']
        res = []
        def all_options(arr ,k, loc, new_item):
            if len(new_item) == k:
                res.append(new_item.copy())
                return True

            for i in range(loc,len(arr)):
                new_item.append(arr[i])
                all_options(arr,k,i,new_item)
                new_item.pop()

        all_options(arr,n,0,[])
        return len(res)

if __name__ == '__main__':
    print(Solution().countVowelStrings(1))
    print(Solution().countVowelStrings(2))
    print(Solution().countVowelStrings(33))



