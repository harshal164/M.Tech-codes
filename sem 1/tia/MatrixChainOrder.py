#!/usr/bin/env python3
def order(p):
    n = len(p) - 1;
    m = [[0 for _ in range(n+1)] for _ in range(n+1)]
    s = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        m[i][i] = 0
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j = i+l-1
            m[i][j] = 555555555555 #INFINITY
            for k in range(i,j):
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m,s,n

def main():
    p = list(map(int,input().split(" ")))
    m,s,n = order(p)
    print(m[1][n])
    printOptimalParens(s,1,n)
    print("")

def printOptimalParens(s,i,j):
    if i == j:
        print("M{}".format(i),end="")
    else:
        print("(",end="")
        printOptimalParens(s,i,s[i][j])
        printOptimalParens(s,s[i][j]+1,j)
        print(")",end="")

if __name__ == "__main__":
    main()
