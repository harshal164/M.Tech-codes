class node:
    def __init__(self):
        self.flag=False
        self.d=55555
        self.pi=None

l = []
filename = 'sample_for_bellman_ford'
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

edge_list=[]
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        # print(j)
        if adj_matrix[i][j]!=0:
            edge_list.append([i,j])
print(edge_list)
node_list[0].d=0
for i in range(len(adj_matrix)-1):
    for e in edge_list :
        if node_list[e[1]].d>node_list[e[0]].d+adj_matrix[e[0]][e[1]]:
            node_list[e[1]].d = node_list[e[0]].d + adj_matrix[e[0]][e[1]]
            node_list[e[1]].pi=e[1]

    for e in edge_list:
        if node_list[e[1]].d > node_list[e[0]].d + adj_matrix[e[0]][e[1]]:
            node_list[e[1]].d = node_list[e[0]].d + adj_matrix[e[0]][e[1]]
            node_list[e[1]].pi = e[1]
print("distance parent")
for i in range(len(node_list)):
    print(node_list[i].d,node_list[i].pi)