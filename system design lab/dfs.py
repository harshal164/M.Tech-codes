import math



l=[]
filename = 'dfs_input'
with open (filename, "r") as f:
  l=list(f.read())
l=list(filter(lambda a: a != "\n", l))
# print(l)
no_of_nodes=int(math.sqrt(len(l)))
adjacency_list=dict()

for i in range(no_of_nodes):
    for j in range(no_of_nodes):
       if l[no_of_nodes*i+j]=='1':

           if adjacency_list.get(i):
               # print(i, j)
               adjacency_list[i].append(j)
               # print(adjacency_list)
           else:

               adjacency_list[i]=[j]
               # print(adjacency_list)
print(adjacency_list)

visited = []

def dfs(graph,node):
    global visited
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n)


def bfs(graph,node):

    visited = [False] * (len(graph))
    queue=[]
    queue.append(node)
    visited[node] = True

    while queue:
        n = queue.pop(0)
        print(n, end=" ")
        for i in graph[n]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

dfs(adjacency_list,0)
print(visited)
bfs(adjacency_list,0)