'''
2038. Remove Colored Pieces if Both Neighbors are the Same Color

array
Medium
https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/description/

'''
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        number_of_turns = {"A":0,"B":0}
        end = len(colors)
        p1 = 2
        p2 = 1
        p3 = 0

        while p1 < end:
            if colors[p1] == colors[p2] and colors[p2] == colors[p3]:
                number_of_turns[colors[p1]] +=1
            p1+=1
            p2+=1
            p3+=1
        if number_of_turns['A'] == number_of_turns['B'] or number_of_turns['A'] < number_of_turns['B']:
            return False
        return True