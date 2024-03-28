'''
30\10\23
890.Find and Replace Pattern
Hash Map
Medium
https://leetcode.com/problems/find-and-replace-pattern/submissions/
Acceptance Rate
77.1%. Submissions
229.5K. Accepted
177K
'''

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for new_word in words:
            obj = dict()
            flag = True
            if len(new_word) == len(pattern):
                for idx, letter in enumerate(new_word):
                    if pattern[idx] in obj:
                        print(obj, pattern[idx], letter)
                        if obj[pattern[idx]] != letter:
                            flag = False
                            break
                    else:
                        obj[pattern[idx]] = letter
            if self.obj_is_valid(obj) and flag:
                res.append(new_word)
        return res

    def obj_is_valid(self, obj):
        temp = dict()
        for k, v in obj.items():
            if v in temp:
                return False
            else:
                temp[v] = 1
        return True

'''
"class Solution:
	def findAndReplacePattern(self, words: List[str], p: str) -> List[str]:
		def find(w): # function thats calculate the numeric pattern
			l = []
			m = defaultdict(int)
			i = 0
			for c in w:
				if c in m:
					l.append(m[c])
				else:
					i+=1
					m[c]=i
					l.append(m[c])
			return l
		ans = []
		pfind = find(p)
		for w in words:
			wfind = find(w)
			if wfind == pfind: ans.append(w) #check if numeric pattern of pattern is equal to pattern of word 
		return ans"


'''