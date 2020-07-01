class node:
    def __init__(self):
        self.flag=False
        self.d=55555
        self.pi=None

l = []
filename = 'weighted_graph'
with open(filename, "r") as f:
    l = list(f.read())
adj_matrix=[]
for i in range(len(l)):
    if '\n' in  l:
        temp=l[:l.index('\n')]
        temp1=''.join(temp)
        adj_matrix.append(list(map(int,(temp1.split(',')))))
        l=l[(l.index('\n')+1):]
adj_matrix.append(list(map(int,''.join(l).split(','))))
print(adj_matrix)

node_list=[]
for i in adj_matrix:
    node_list.append(node())
def minimum():
    global node_list,adj_matrix
    unmarked=[]
    for i in range(len(node_list)):
    # print(unmarked)
        if node_list[i].flag==False:
            unmarked.append(i)

    min=unmarked[0]
    for i in unmarked:
        if node_list[i].d<node_list[min].d:
            min=i
    return min

# node_list[0].d = 0
def prim(s,destination):
    global adj_matrix,node_list


    node_list[0].d=0
    # node_list[s].flag=True

    for k in range(len(node_list)):
        u=minimum()
        # print(u)
        for v in range(len(adj_matrix[u])):
            if adj_matrix[u][v]!=0:
                # print("u:",u,"v:",v,adj_matrix[u][v],node_list[v].d)
                if node_list[v].flag==False:
                    # print((node_list[v].d,(node_list[u].d+adj_matrix[u][v])))
                    if (node_list[v].d>(adj_matrix[u][v])):
                        node_list[v].d=(adj_matrix[u][v])
                        node_list[v].pi=u
        node_list[u].flag=True



prim(0,4)
for i in range(len(node_list)):
    print(i,node_list[i].d,node_list[i].pi)

