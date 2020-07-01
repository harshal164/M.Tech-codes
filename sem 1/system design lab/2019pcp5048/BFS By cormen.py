import math


class node:
    def __init__(self):
        self.color = 'white'
        self.d = 5555
        self.pi = None
        # self.arrival_time=0
        # self.removal_time=0

# queue = []
l = []
filename = 'dfs_input'
with open(filename, "r") as f:
    l = list(f.read())
l = list(filter(lambda a: a != "\n", l))
# print(l)
no_of_nodes = int(math.sqrt(len(l)))
node_list = []
for x in range(no_of_nodes):
    node_list.append(node())
adjacency_list = dict()

for i in range(no_of_nodes):
    for j in range(no_of_nodes):

        if l[no_of_nodes * i + j] == '1':
            if adjacency_list.get(i):
                # print(i, j)
                adjacency_list[i].append(j)
            # print(adjacency_list)

            else:
                adjacency_list[i] = [j]
            # print(adjacency_list)
print(adjacency_list)


# print(node_list)


def BFS(graph, s, node_list):
    node_list[s].color = 'grey'
    node_list[s].d = 0
    node_list[s].pi = None
    # node_list[s].arrival_time=1
    time=1
    queue = []
    queue.append(s)
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            # time+=1
            if node_list[v].color == 'white':
                node_list[v].color = 'grey'
                node_list[v].d = node_list[u].d + 1
                node_list[v].pi = u
                node_list[v].arrival_time=time
                # time+=1
                queue.append(v)
        node_list[u].color = 'black'
        # node_list[u].removal_time=time
        # time+=1
        print("selected: ", u, " distance: ", node_list[u].d)


BFS(adjacency_list, 0, node_list)
