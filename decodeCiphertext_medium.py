'''
23\01\24


2075. Decode the Slanted Ciphertext

array 2D

Medium
https://leetcode.com/problems/decode-the-slanted-ciphertext/description/

"Accepted
12.6K
Submissions
25.6K
Acceptance Rate
49.2%"


"Run time Beats51.75%of users with Python3,Memory Beats
10.53%
of users with Python3"

'''


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        COLS = int(len(encodedText) / rows)
        matrix = []
        i = -1
        for idx, w in enumerate(encodedText):
            if idx % (COLS) == 0:
                i += 1
                matrix.append([])
            matrix[i].append(w)
        print(matrix)

        res = ''
        for i in range(COLS):
            for row in matrix:
                if i < COLS:
                    res += row[i]
                i += 1

        return res.rstrip()



'''
"class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols, res = len(encodedText) // rows, """"
        for i in range(cols):
            for j in range(i, len(encodedText), cols + 1):
                res += encodedText[j]
        return res.rstrip()"

'''







