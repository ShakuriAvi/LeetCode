'''
02\04\24

777. Swap Adjacent in LR String
string

Medium

https://leetcode.com/problems/swap-adjacent-in-lr-string/description/

Accepted
75.3K
Submissions
204.6K
Acceptance Rate
36.8%

'''

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        queue = [start]
        visited = set()
        while queue:
            node = queue.pop(0)
            if node == end:
                return True
            if node in visited:
                continue

            for i in range(len(node)):
                if i+1 < len(node):
                    curr_string = node[i] + node[i + 1]
                    if curr_string == "XL":
                        queue.append(node[:i] + "LX" + node[i+2:])
                        visited.add(node)
                    elif curr_string == "RX":
                        queue.append(node[:i]+"XR"+node[i+2:])
                        visited.add(node)
        return False


if __name__ == '__main__':
    print(Solution().canTransform("RXXLRXRXL","XRLXXRRLX"))