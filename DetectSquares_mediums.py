from typing import List
from functools import reduce
class DetectSquares:

    def __init__(self):
        self.xis = dict()
        self.yis = dict()
        pass

    def add(self, point: List[int]) -> None:
        self.__insert_to_x_dict(point)
        self.__insert_to_y_dict(point)


    def __insert_to_x_dict(self, point:List[int]):
        x = point[0]
        if x not in self.xis:
            self.xis[x] = dict()
        y = point[1]
        if y not in self.xis[x]:
            self.xis[x][y] = 0
        self.xis[x][y] += 1

    def __insert_to_y_dict(self, point: List[int]):
        y = point[1]
        if y not in self.yis:
            self.yis[y] = dict()
        x = point[0]
        if x not in self.yis[y]:
            self.yis[y][x] = 0
        self.yis[y][x] += 1

    def count(self, point: List[int]) -> int:
        stack = [(point[0], point[1], [1])]
        res = 0
        while stack:
            x1, y1, options = stack.pop()
            if len(options) == 4:
                if point[0] == x1 or y1 == point[1]:
                    res = max(res, self.__calculate_options(options))
                continue

            if len(options) % 2 == 0:
                if x1 in self.xis:
                    for y2, v in self.xis[x1].items():
                        temp_option = options.copy()
                        temp_option.append(v)
                        stack.append((x1, y2, temp_option))
            else:
                if y1 in self.yis:
                    for x2, v in self.yis[y1].items():
                        temp_option = options.copy()
                        temp_option.append(v)
                        stack.append((x2, y1, temp_option))
        return res

    def __calculate_options(self, options: list) -> int:
        return reduce(lambda x, y: x*y, options)






if __name__ == '__main__':
    # Your DetectSquares object will be instantiated and called as such:
    # obj = DetectSquares()
    # obj.add(point)
    # param_2 = obj.count(point)
    detectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    print(detectSquares.count([11, 10]))
    detectSquares.add([11, 2])
    print(detectSquares.count([11, 10]))
