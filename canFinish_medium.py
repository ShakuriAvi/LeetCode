'''
29\06\24
207. Course Schedule
https://leetcode.com/problems/course-schedule/description/

Accepted
1.6M
Submissions
3.4M
Acceptance Rate
47.0%

Memory
18.15
MB
Beats
88.71%


Runtime
92
ms
Beats
42.91%

'''

from typing import List
from collections import defaultdict
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be popped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        my_graph = Graph(numCourses)
        while prerequisites:
            course, require = prerequisites.pop()
            my_graph.addEdge(course, require)

        if my_graph.isCyclic() == 1:
            return False
        else:
            return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(2, [[1,0]]))
    print(sol.canFinish(2, [[1,0],[0,1]]))

