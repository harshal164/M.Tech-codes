class node:
    def __init__(self):
        self.p = self
        self.rank = 0

class edge:
    def __init__(self,u,v,w):
        self.u=u
        self.v=v
        self.w=w


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




def link(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
    if x.rank == y.rank:
        y.rank += 1


def find_set(x):
    if x != x.p:
        x.p = find_set(x.p)
    return x.p


def union(x, y):
    link(find_set(x), find_set(y))

edge_list=[]
for i in range(len(adj_matrix)):
    for j in range(i,len(adj_matrix)):
        if adj_matrix[i][j]!=0:
            edge_list.append(edge(i,j,adj_matrix[i][j]))
edge_list.sort(key=lambda x:x.w)

node_list=[node() for i in range(len(adj_matrix))]

def kruskal():
    a =list()
    sample_set = set()
    while edge_list:
        temp=edge_list.pop(0)
        if find_set(node_list[temp.u])!=find_set(node_list[temp.v]):
            a.append(temp)
            union(node_list[temp.u],node_list[temp.v])
    return a

x=(kruskal())
for i in  x:
    print(i.u,i.v,i.w)



# for i in edge_list:
#     print(i.w,end=",")
