


a=[[2,3,1,5],[6,13,5,19],[2,19,10,23],[4,10,11,31]]
n=len(a)
l=[[0 for j in range(n)] for i in range(n)]
u=[[0 for j in range(n)] for i in range(n)]
u[0]=a[0]

for i in range(n):
    l[i][i] = 1
    # l[i][0]=a[i][0]/a[0][0]

# print(U,"\n",L)
for k in range(n):
    u[k][k] = a[k][k]
    for i in range(k+1,n):
        l[i][k]=a[i][k]/u[k][k]
        u[k][i]=a[k][i]
    for i in range(k+1,n):
        for j in range(k+1,n):
            a[i][j]=a[i][j]-l[i][k]*u[k][j]
print(u)
print(l)


