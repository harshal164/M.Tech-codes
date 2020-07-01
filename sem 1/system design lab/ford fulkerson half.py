class node:
    def __init__(self):
        self.flag=False
        self.d=55555
        self.pi=None

l = []
filename = 'sample_ford_fulkerson'
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
# print(edge_list)
node_list[0].d=0

# F=0
# min=5555
# def modified_dfs(adj_matrix,s,d, flag):
#     global min
#     if s==d:
#         print(s)
#         flag=1
#         return
#     if flag==1:
#         min=5555
#     # print(adj_matrix[s])
#     print(adj_matrix[s])
#     for i in  range(len(adj_matrix[s])):
#         if adj_matrix[s][i]!=0:
#             if min>adj_matrix[s][i]:
#                 min=adj_matrix[s][i]
#
#             modified_dfs(adj_matrix,i,d,flag)
#             adj_matrix[s][i] -= min
#
#
# s=0
# d=3
# # while modified_dfs(adj_matrix,s,d):
# modified_dfs(adj_matrix,s,d,0)
# print(adj_matrix)
# for i in adj_matrix[s]:
#     if i!=0:
#         min=5555
#         modified_dfs(adj_matrix,s,d,0)
# print(adj_matrix)

# An Iterative Python program to do DFS traversal from
# a given source vertex. DFS(int s) traverses vertices
# reachable from s.

# This class represents a directed graph using adjacency
# # list representation
# class Graph:
#     def __init__(self,V):
#         self.V = len(adj_matrix)
#         self.adj = [[] for i in range(V)]
#
#     def addEdge(self,v, w):
#         self.adj[v].append(w)
#
#
#
#     def DFS(self,s,d):
#
#         visited = [False for i in range(self.V)]
#         stack = []
#         stack.append(s)
#         while (len(stack)):
#             s = stack[-1]
#             stack.pop()
#             if (not visited[s]):
#                 print(s,end=' ')
#                 visited[s] = True
#             for node in self.adj[s]:
#                 if (not visited[node]):
#                     if s==d:
#                         print("at d")
#                         break
#                     stack.append(node)
#
#
# g=Graph(len(adj_matrix))
# for i in  range(len(adj_matrix)):
#     for j in range(len(adj_matrix)):
#         if adj_matrix[i][j]!=0:
#             g.addEdge(i,j)
# g.DFS(0,3)

s=0
d=0
pi=[-1 for i in range(len(adj_matrix))]
def dfs1(adj_matrix,s,d):
    global pi
    f = 0

    while True:

        visited = [False for i in range(len(adj_matrix))]
        stack=[]
        min=5555
        stack.append(s)
        print(stack)
        flag=False
        while len(stack) and not flag:
            temp = stack.pop()
            visited[temp] = True
            for i in range(len(adj_matrix)):
                # s = stack.pop()
                # visited[s]=True
                if visited[i]==False and adj_matrix[temp][i]!=0:
                    print(i)
                    visited[i]=True
                    pi[i]=temp
                    if d==i:
                        flag=1
                        # stack.append(i)
                        stack=[]

                    if min>adj_matrix[temp][i]:
                        min=adj_matrix[temp][i]
                    stack.append(i)
                    if flag:
                        # continue
                        break
            # visited[temp]=True
        temp=d

        if visited[temp]:
            while pi[temp]!=-1:
                adj_matrix[pi[temp]][temp]+=min
                adj_matrix[temp][pi[temp]]-=min
                f+=min
                temp=pi[temp]
                print(visited)

        else:
            print("here")
            break
    return f
print(adj_matrix)
print(dfs1(adj_matrix,s,d))