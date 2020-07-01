a=[[1,2],[4,5],[8,9]]
b=[[2,4,5,6],[6,5,4,9]]
c=[[0 for j in range(len(b[0]))] for i in range(len(a))]
print(c)

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(a[0])):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]

print(c)