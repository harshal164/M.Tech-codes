class Node:
    def __init__(self,i):
        value=i
with open('transaction') as f:
    # while f:

    trans=(f.readlines())
    no_of_trans=int(trans[0][:-1])
    # print(no_of_trans)
    trans=trans[1:]
    # print(trans)
    nodes=[Node(i) for i in range(1,no_of_trans+1)]
    adj_matrix=[[0 for i in range(no_of_trans+1)]for j in range(no_of_trans+1)]
    # print(adj_matrix)
    for i in range(len(trans)):
        if trans[i][0]=='R':
            for j in range(i+1,len(trans)):
                if trans[i][1]!=trans[j][1] and trans[j][0]=='W' and trans[i][3]==trans[j][3]:
                    adj_matrix[int(trans[i][1])][int(trans[j][1])]=1
        if trans[i][0] == 'W':
            for j in range(i + 1, len(trans)):
                if trans[i][1] != trans[j][1]  and trans[i][3] == trans[j][3]:
                    adj_matrix[int(trans[i][1])][int(trans[j][1])]=1
    ll=[]
    color = ['white' for i in range(len(adj_matrix) + 1)]
    def DFS(i):
        color[i]='grey'
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1 and color[j] == 'white':
                color[j]='grey'
                DFS(j)
            elif adj_matrix[i][j] == 1 and color[j] == 'grey':
                print("not conflict serializable")
                exit(0)
        color[i]='black'
        ll.insert(0,i)
    # print(adj_matrix)
    for i in range(len(adj_matrix)):
        if color[i]=='white':
            DFS(i)


    # print(color)
    ll.remove(0)
    ll=map(str,ll)

    print('->'.join(ll))