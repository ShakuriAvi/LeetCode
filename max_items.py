
class Solution:
    def get_max_items(self, items :list) -> int:
        position_y, counter = 0, 0
        items_by_position = self.__create_items_by_position(items)
        for x ,loc in items_by_position:
            if loc == "S":
                counter += 1
                position_y = max(position_y, counter)
            else:
                counter -= 1
        return position_y

    def __create_items_by_position(self, items: list) -> list:
        items_by_position = []
        for item in items:
            items_by_position.append((item[0], "S"))
            items_by_position.append((item[1], "E"))

        items_by_position = sorted(items_by_position, key=lambda k: k[0])
        return items_by_position


if __name__ == "__main__":
    items = [(1,3), (2,3.5), (2.5,5), (4,4.5), (4.5,6)]
    sol = Solution()
    sol.get_max_items(items)
