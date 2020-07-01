n=int(input("enter no of elements in list"))
print("enter elements separated by spaces")

arr=list(map(int,input().split()))
if len(arr)!=n:
    print("please enter exact no of elements that are sepcified")
    exit(0)

for i in range(n):
    for j in  range(i+1,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print(arr)
