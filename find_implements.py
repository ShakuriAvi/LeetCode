from complete_binary_tree_inserter_medium import buildTree
import os
def bfs(root:str, target:str)->str:
    queue = [root]
    while queue:
        item = queue.pop(0)
        root = item.split("/")[-1]
        subs_dir = ls(item) if item.isdir() else []
        if not item.isdir() and root == target:
            return item

        for sub in subs_dir:
            queue.append(f"{item}/{sub}")

    return None



if __name__ == '__main__':
    bfs("windows", "documents")