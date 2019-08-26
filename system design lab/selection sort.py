import random
n=int(input("enter no of elements in list"))
print("enter elements separated by spaces")

arr=list(map(int,input().split()))
if len(arr)!=n:
    print("please enter exact no of elements that are sepcified")
    exit(0)
for i in range(n):
    min = i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min=j
    arr[min],arr[i]=arr[i],arr[min]

print(arr)

(random.shuffle(arr))
print("array after randomized:",arr)