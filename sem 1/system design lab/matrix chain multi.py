m = [[10000 for _ in range(1000)] for _ in range(1000)]
s = [[0 for _ in range(1000)] for _ in range(1000)]
def RECURSIVE_MATRIX_CHAIN(p,i,j):
    global m
    global s
    if m[i][j] < 10000:
        return m[i][j]
    if i == j:
        return 0
    for k in range(i,j):
        q=RECURSIVE_MATRIX_CHAIN(p,i,k)+RECURSIVE_MATRIX_CHAIN(p,k+1,j)+p[i-1]*p[k]*p[j]
        if q < m[i][j]:
            m[i][j]=q
            s[i][j]=k
    return m[i][j]

def printparens(s,i,j):
    if i == j:
        print("A"+str(i+1),end=" ")
    else:
        print("(",end="")
        printparens(s,i,s[i][j])
        printparens(s,s[i][j]+1,j)
        print(")",end="")

p = [10,5,8,2,10,4]
x = RECURSIVE_MATRIX_CHAIN(p,0,4)
print(x)
printparens(s,0,4)