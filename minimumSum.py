'''
28\06\24
2829. Determine the Minimum Sum of a k-avoiding Array
https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/description/
Accepted
34.2K
Submissions
55.9K
Acceptance Rate
61.2%

Memory
16.50
MB
Beats
78.46%


Runtime
41
ms
Beats
70.26%
'''

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        val_by_sum = dict()
        count = 1
        while n != 0:
            i = count
            if i not in val_by_sum:
                val_by_sum[k-i] = i
                n -= 1
            count += 1

        return sum(val_by_sum.values())
if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumSum(5,4))
    print(sol.minimumSum(2,6))
