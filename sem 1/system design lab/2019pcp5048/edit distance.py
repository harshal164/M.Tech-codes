str1=input("enter string 1")
str2=input("enter string 2")


def edit_distance(str1,str2):
    table=[[0 for j in range(len(str1)+1)] for i in range(len(str2)+1) ]
    for i in range(1,len(str1)+1):
        table[0][i]=i
    for i in range(len(str2)+1):
        table[i][0] = i

    print(table)
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str2[i]==str1[j]:
                table[i+1][j+1]=min(table[i][j],table[i][j+1],table[i+1][j])
            else:
                table[i+1][j+1]=min(table[i][j],table[i][j+1],table[i+1][j])+1
    print(table)
    return table[len(str2)][len(str1)]


print(edit_distance(str1,str2))