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
    def changed_graph_direction(self):
        reversed_graph = dict()
        for node in range(self.V):
            items = self.graph[node]
            for item in items:
                if item not in reversed_graph:
                    reversed_graph[item] = []
                reversed_graph[item].append(node)
        return reversed_graph

    def order_courses(self):
        degree = [0] * self.V

        for i in range(self.V):
            if i in self.graph:
                degree[i] = len(self.graph[i])

        return [i[0] for i in sorted(enumerate(degree), key=lambda x:x[1])]


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        my_graph = Graph(numCourses)
        items = prerequisites.copy()
        while items:
            course, require = items.pop()
            my_graph.addEdge(course, require)

        if my_graph.isCyclic() == 1:
            return []
        else:
            return my_graph.order_courses()


if __name__ == '__main__':
    sol = Solution()
    # print(sol.findOrder(2, [[1,0]]))
    print(sol.findOrder(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))

