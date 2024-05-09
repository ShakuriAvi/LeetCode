from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def lexical_calculate(num):
            if n < num:
                return
            res.append(num)
            for i in range(10):
                lexical_calculate(num*10+i)

        for i in range(1, 10):
            lexical_calculate(i)
        return res



if __name__ == '__main__':
    print(Solution().lexicalOrder(100))


