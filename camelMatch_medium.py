'''
31\03\24

1023. Camelcase Matching

string

Medium

https://leetcode.com/problems/camelcase-matching/description/

Accepted
47.2K
Submissions
76K
Acceptance Rate
62.1%

'''

from typing import List
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        queue_pattern = self.__insert_word_to_queue(pattern)
        res = []
        for query in queries:
            queue_query = self.__insert_word_to_queue(query)
            is_valid = self.__check_if_pattern_in_word(queue_pattern.copy(), queue_query)
            res.append(is_valid)
        return res

    def __check_if_pattern_in_word(self, pattern, query):
        for q in query:
            if q.isupper():
                if len(pattern) == 0 or q != pattern[0]:
                    return False
                elif q == pattern[0]:
                    pattern.pop(0)
            elif len(pattern) > 0:
                if q == pattern[0]:
                    pattern.pop(0)

        if len(query):
            return False
        return True


    def __insert_word_to_queue(self, pattern):
        return [pat for pat in pattern]




if __name__ == '__main__':
    print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"))



