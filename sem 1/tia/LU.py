#!/usr/bin/env python3
def LU():
    tmp = list(map(int,input().split("\n")))
    n = tmp[0]
    A = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = list(map(int,input().split("\n")))
            A[i][j] = tmp[0]
    L = [[0 for _ in range(n)] for _ in range(n)]
    U = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            U[i][j] = 0
    for i in range(n):
        L[i][i] = 1
        for j in range(i+1,n):
            L[i][j] = 0
    for k in range(n):
        U[k][k] = A[k][k]
        for i in range(k+1,n):
            L[i][k] = A[i][k]/U[k][k]
            U[k][i] = A[k][i]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j] = A[i][j] - L[i][k]*U[k][j];
    return L,U,n

def main():
    L,U,n = LU()
    print("L = ")
    for i in range(n):
        for j in range(n):
            print(int(L[i][j]),end=' ')
        print("")
    print("U = ")
    for i in range(n):
        for j in range(n):
            print(int(U[i][j]),end=' ')
        print("")

if __name__ == "__main__":
    main()
