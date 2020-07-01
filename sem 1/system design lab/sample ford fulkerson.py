def func(adj_matrix,s,d):
    min=5555
    visited=[]
    # visited.append(s)
    for i in range(len(adj_matrix)):

        for j in range(len(adj_matrix)):
            if adj_matrix[i][j]!=0 and not visited[j]:
                visited.append(j)
                if min>adj_matrix[i][j]:
                    min=adj_matrix[i][j]
                i=j
            if i==d:
                # for i in visited:
                print(visited)
                # for i in range(len(adj_matrix)):
                #     for j in range(len(adj_matrix)):
                #         if adj_matrix[i][j] >min:
                #             adj_matrix[i][j]-=min

                            # visited.append(j)
                            # if min > adj_matrix[i][j]:
                            #     min = adj_matrix[i][j]
                for i in range(len(adj_matrix)):

                    for j in visited:
                        if adj_matrix[i][j]>=min:
                            adj_matrix[i][j]-=min
                            adj_matrix[j][i] += min
                            break


                return min
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
s=0
d=3



print(func(adj_matrix,s,d))

print(adj_matrix)

while adj_matrix[0].count(0)!=len(adj_matrix):
    print(func(adj_matrix, s, d))