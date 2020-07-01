from random import randint
MAX_LENGTH=32
INT_MAX_LENGTH=32
f=open('sample_for_bit_vector')
inp=list(f.read())
ind=inp.index('\n')
n=int(''.join(inp[:ind]))
inp=inp[(ind+1):]
# print("n: ",n)

sets=[]

for i in range(len(inp)):
    if '\n' in inp:
        newline_ind=inp.index('\n')
        x=inp[:newline_ind]

        inp=inp[newline_ind+1:]

        sets.append(x)

sets.append(inp)




for i in range(len(sets)):
    sets[i]=''.join(sets[i])
    sets[i]=list(map(int,sets[i].split(' ')))
# print("sets: ",sets)


arr=[]
for i in range(len(sets)):
    temp=[]
    for i in range(1000//INT_MAX_LENGTH+1):
        temp.append(0)
    arr.append(temp)

# print("arr ",arr)


def union(arr):
    global sets
    length=len(sets)
    a,b=list(map(int,input("enter which two sets you want to merge:").split()))
    print(a,b)
    temp=[]
    for i in range(1000//INT_MAX_LENGTH+1):
        temp.append(arr[a][i] | arr[b][i])
    print("after merging bit array:",temp)
    print("NOTICE: original bit array is unchanged")

def difference(arr):
    global sets
    length = len(sets)
    a, b = list(map(int, input("enter which two sets you want to find difference:").split()))
    print(a, b)
    b= b
    temp = []
    for i in range(1000 // INT_MAX_LENGTH + 1):
        temp.append(arr[a][i] & ~arr[b][i])
    print("after difference bit array:", temp)
    print("NOTICE: original bit array is unchanged")


def intersect(arr):
    global sets
    length=len(sets)
    a,b=list(map(int,input("enter which two sets you want to merge:").split()))
    print(a,b)
    temp=[]
    for i in range(1000//INT_MAX_LENGTH+1):
        temp.append(arr[a][i] &arr[b][i])
    print("after merging bit array:",temp)
    print("NOTICE: original bit array is unchanged")



def membership(arr):
    n=int(input("enter element to check membership"))
    index=n//32
    offset=n%32
    mask=1
    mask<<=offset

    for i in range(len(arr)):
        if (arr[i][index]&mask):
            print(i)


def print_set(arr):
    n=int(input("enter set no to print"))
    temp=arr[n]
    print(temp)
    for i in range(len(temp)-1,-1,-1):
        # print("{0:b}".format(temp[i]),end='')
        x=bin(temp[i])
        x1=''.join(list(x)[2:])
        print(x1.zfill(32))
        # print(x1)


for i in range(len(sets)):
    # print("i==",i)
    for k in sets[i]:

        index=k//32
        offset=k%32
        # print("index of",k,"is ",index,"offset,",offset)
        temp=1<<offset
        arr[i][index]=arr[i][index]|temp

        # for j in range(MAX_LENGTH-1,-1,-1):
        #     if j == (k):
        #         print("1 at position",j)
                # arr[i][index]=arr[i][index]<<1
                # arr[i][index]=arr[i][index]|1
                # print(arr[i])

            # else:
            #     print("J= ", j)
            #     arr[i][index]=arr[i][index]<<1
            #     print(arr[i])


# for i in arr:
#     print("{0:b}".format(i))
# print(arr)
# union(arr)

# membership(arr)
# print_set(arr)

# intersect(arr)
while(True):
    print("1. union\n 2. print set \n 3. intersect \n 4. difference")
    options={'1':union,'2':print_set,'3':intersect,'4':difference}
    i = input("enter q to quit")
    # print(options[i])
    if i=='q':
        break
    options[i](arr)

print("good bye")