'''
23\01\24


352. Data Stream as Disjoint Intervals

sliding window, Array


Hard

https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/

"Accepted
104.7K
Submissions
174.9K
Acceptance Rate
59.9%"



"Run time Beats90.86%of users with Python3, Memory Beats
78.43%
of users with Python3"


'''

from typing import List

class SummaryRanges:

    def __init__(self):
        self.big_num = 0
        self.array = [0]
        

    def addNum(self, value: int) -> None:
        if value > self.big_num:
            self.big_num = value
            self.array = self.array + [0]*(self.big_num-len(self.array)+1)
        self.array[value] = 1
       
        

    def getIntervals(self) -> List[List[int]]:
        start,end = 0,0
        intervals = dict()
        while end < len(self.array):
            if self.array[start] == 1:
                end = start+1
                while end < len(self.array) and self.array[end] == 1 :
                    end+=1
                intervals[start] = end-1
                start = end
            else:
                start+=1
                end+=1
        res = []
        for k,v in intervals.items():
            if k >=0: 
                res.append([k,v])
        return res

        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

'''
"class SummaryRanges:
    def __init__(self):
        self.intervals = set()

    def addNum(self, value: int) -> None:
        self.intervals.add(value)

    def getIntervals(self) -> List[List[int]]:
        ans = []
        arr = sorted(self.intervals)
        start, end = arr[0], arr[0]
        for curr in arr[1:]:
            if end+1 == curr:
                end = curr
            else:
                ans.append([start, end])
                start, end = curr, curr
        ans.append([start, end])
        return ans"

'''