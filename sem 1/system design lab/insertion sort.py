n=int(input("enter no of elements in list"))
print("enter elements separated by spaces")

arr=list(map(int,input().split()))
if len(arr)!=n:
    print("please enter exact no of elements that are sepcified")
    exit(0)

for i in range(1,n):
    temp=arr[i]
    j=i-1
    while(j>=0 and temp<arr[j]):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp
print(arr)