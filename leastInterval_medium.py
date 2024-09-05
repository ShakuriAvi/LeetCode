from typing import List
from queue import PriorityQueue
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        sorted(tasks)
        cool_by_item = dict()
        queue = PriorityQueue()
        while tasks:
            item = tasks.pop(0)
            if item not in cool_by_item:
                cool_by_item[item] = 0
            cool_by_item[item] += 1
            queue.put((cool_by_item[item], item))

        count = 0
        days_by_item = dict()
        days = []
        while not queue.empty():
            priority, item = queue.get()
            if item not in days_by_item:
                days_by_item[item] = count + n
                days.append(item)

            else:
                if days_by_item[item] < count:
                    days.append(item)
                    days_by_item[item] = count + n
                else:
                    days.append(-1)
                    queue.put((priority, item))
            count += 1
        return len(days)





    def sorted_by_shows(self, tasks: List[str],) -> int:
        item_by_count = dict()
        for task in tasks:
            if task not in item_by_count:
                item_by_count[task] = 0
            item_by_count[task] += 1





if __name__ == '__main__':
    sol = Solution()
    # print(sol.leastInterval(["A","A","A","B","B","B"], 2))
    print(sol.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 1))
