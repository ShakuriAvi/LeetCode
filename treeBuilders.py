from typing import Any


class BinaryTree:
    def __init__(self, root: int):
        self.val = root
        self.left = None
        self.right = None


def from_lst_to_binary_tree(lst: list):
    if len(lst) == 0:
        return None
    main_root = BinaryTree(lst.pop(0))
    queue = [main_root]
    while queue:
        root = queue.pop(0)
        if root.val is None:
            continue
        left_root = __insert_node("left", root, lst)
        if left_root:
            queue.append(left_root)
        right_root = __insert_node("right", root, lst)
        if right_root:
            queue.append(right_root)

    return main_root


def __insert_node(side: str, root: BinaryTree, lst: list) -> Any:
    if len(lst) > 0 and root.val is not None:
        if lst[0] is not None:
            new_root = BinaryTree(lst.pop(0))
            if side == "left":
                root.left = new_root
            else:
                root.right = new_root

        else:
            new_root = lst.pop(0)

        return new_root

    return None


def print_binary_tree(root: BinaryTree):
    queue = [root]
    while queue:
        root = queue.pop(0)
        print(root.val)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)


if __name__ == '__main__':
    print_binary_tree(from_lst_to_binary_tree([3, 9, None, 15, 7, 4, 8]))
    print_binary_tree(from_lst_to_binary_tree([3, 4, 7, 8, 9, 20, 15]))
