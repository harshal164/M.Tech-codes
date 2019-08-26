import math,copy
class node:
    def __init__(self):
        self.color = 'white'
        self.d = 5555
        self.pi = None
        self.discovery_time = 0
        self.removal_time = 0

l = []
filename = 'smple_for_connected'
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


# print(node_list)
time = 0



def transpose_graph(graph,node_list):
    transposed=dict()
    global time
    time=0
    for i in node_list:

        i.color="white"
        i.discovery_time=0
        i.pi=None
        i.removal_time=0

    for key in graph:
        transposed[key] = []

    for key in graph:

        out_going=graph[key]
        for i in out_going:
            if transposed.get(i):
                transposed[i].append(key)
            else:
                transposed[i]=[key]
    return transposed



def modified_dfs(transposed_graph,s,node_list):

    if node_list[s].color == "white":
        print(s)
        node_list[s].color='grey'

        for i in transposed_graph[s]:

            modified_dfs(transposed_graph, i, node_list)




def strongly_connected_components(transposed_graph,s,node_list,finish_time):
    counter_for_node=copy.deepcopy(finish_time)
    while counter_for_node:
        maximum_value = max(finish_time)
        ind = finish_time.index(maximum_value)
        finish_time[ind] = 0
        if node_list[ind].color=='white':
            print("batch")
            modified_dfs(transposed_graph,ind,node_list)

        counter_for_node.pop()




def DFS_VISIT(graph, s,node_list):
    global time
    time += 1
    node_list[s].discovery_time = time
    node_list[s].color = 'grey'
    print(s)
    for i in graph[s]:
        if node_list[i].color == "white":
            node_list[i].pi = s
            DFS_VISIT(graph, i,node_list)
    node_list[s].color = "black"
    # print(s)
    time += 1
    node_list[s].removal_time = time


def DFS(graph, s, node_list):
    global time
    # node_list[s].color = 'grey'
    node_list[s].d = 0
    node_list[s].pi = None

    node_list[s].discovery_time = 1
    # time = 0

    # stack.append(s)

    for node in adjacency_list:

        # print(node)
        if node_list[node].color == "white":
            # print("for ", node, "dfs called")

            node_list[node].discovery_time=time
            DFS_VISIT(graph, node,node_list)

DFS(adjacency_list, 0, node_list)


for i in range(len(node_list)):
    print("discovery time of ",i,": ",node_list[i].discovery_time," removing time: ",node_list[i].removal_time)

finish_time = []

for i in node_list:
    finish_time.append(i.removal_time)

print("originall", adjacency_list)
transposed_adjacency_list=transpose_graph(adjacency_list,node_list)
print("transposed:",transposed_adjacency_list)
l=strongly_connected_components(transposed_adjacency_list,0,node_list,finish_time)






