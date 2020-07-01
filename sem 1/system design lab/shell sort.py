n=int(input("enter no of elements in list"))
print("enter elements separated by spaces")

arr=list(map(int,input().split()))
if len(arr)!=n:
    print("please enter exact no of elements that are sepcified")
    exit(0)

def shellSort(arr):
    gap=len(arr)//2

    while (gap>0):
        for i in range(gap,n):
            temp=arr[i]
            j=i

            while j>=gap and arr[j-gap]>temp:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=temp
        gap//=2

shellSort(arr)
print(arr)