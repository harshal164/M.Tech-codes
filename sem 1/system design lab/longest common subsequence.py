a =input("enter 1st string")
b =input("enter second string")
table= [[None]*(len(b) + 1) for i in range(len(a) + 1)]
# print(table)


for i in range(len(a) + 1):
    for j in range(len(b) + 1):
        if i == 0 or j == 0 :
            table[i][j] = 0
        elif a[i-1] == b[j-1]:
            table[i][j] = table[i-1][j-1]+1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])

print("longest common subsequence is ",table[len(a)][len(b)])
