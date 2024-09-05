class Graph:
    def __init__(self):
        self.graph = {}
        self.roots = []

        self.printify_item = "-" * 3
    def addEdge(self, u, v):
        if u is None:
            self.roots.append(v)
        else:
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)

    def print_item(self) -> None:

        def dfs(root: dict, level: int) -> None:
            root_pid = root["pid"]
            print(self.printify_item*level + str(root["process_name"]) )
            childs = self.graph[root_pid] if root_pid in self.graph else []
            for item in childs:
                dfs(item, level+1)

        for root in self.roots:
            dfs(root, 0)


def print_graph(process_lst: list) -> None:
    my_graph = Graph()
    for process in process_lst:
        my_graph.addEdge(process["parent_pid"], {"pid": process["pid"], "process_name": process["process_name"]})

    my_graph.print_item()





if __name__ == "__main__":
    process = [{"process_name":"a.exe", "pid":420, "parent_pid":428},

{"process_name":"c.exe", "pid":428, "parent_pid":None},

{"process_name":"d.exe", "pid":551, "parent_pid": 420},

{"process_name":"e.exe", "pid":552, "parent_pid":428},

{"process_name":"f.exe", "pid":553, "parent_pid":None},

{"process_name":"g.exe", "pid":4, "parent_pid":553},

{"process_name":"b.exe", "pid":7, "parent_pid":4},

{"process_name":"h.exe", "pid":11, "parent_pid":7},

{"process_name":"j.exe", "pid":666, "parent_pid":428}]
    print_graph(process_lst=process)
