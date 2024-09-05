'''
01\07\24
1910. Remove All Occurrences of a Substring
https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/

Accepted
120.2K
Submissions
155.1K
Acceptance Rate
77.5%

Memory
16.64
MB
Beats
26.52%

runtime
46
ms
Beats
22.84%

'''

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        start, end = 0, len(part)
        while end <= len(s):
            new_word = s[start:end]

            if new_word == part:
                s = s[:start] + s[end:]
                # while start != end:
                #     s_list[start] = "_"
                #     start += 1
                # while end < len(s) and end < start + len(part):
                #     end += 1
                start, end = 0, len(part)
            else:
                start += 1
                end += 1

        return s



if __name__ == "__main__":
    sol = Solution()
    sol.removeOccurrences("daabcbaabcbc", "abc")
