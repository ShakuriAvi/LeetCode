'''
27\06\24
second attempt
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
Accepted
2M
Submissions
2.9M
Acceptance Rate
66.9%

Memory
17.58
MB
Beats
63.61%


Runtime
51
ms
Beats
89.68%


'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) < 2:
            return res

        buy = prices[0]
        for idx in range(1, len(prices)):
            sell = prices[idx]
            if sell > buy:
                res += sell - buy
            buy = sell
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([1,2,3,2,5]))
    # print(sol.maxProfit([7,6,4,3,1]))


