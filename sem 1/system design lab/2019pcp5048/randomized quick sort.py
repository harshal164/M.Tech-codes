import random
def partition(arr,low,high):
    i=low
    r=random.randint(low,high)
    # pivot=r
    arr[r],arr[low]=arr[low],arr[r]
    pivot=low

    # print("here pivot and i=",pivot,i,high)
    for j in range(low+1,high+1):
        if arr[j]<=arr[pivot]:
            i=i+1
            # print("i j swapped", i,j)
            arr[i],arr[j]=arr[j],arr[i]


    arr[i],arr[pivot]=arr[pivot],arr[i]
    # print(arr[i])
    return i



def quickSort(arr,low,high):
    if low<high:
        correct= partition(arr,low,high)

        quickSort(arr,low,correct-1)
        quickSort(arr,correct+1,high)



if __name__=="__main__":
    n=int(input("enter no of elements in list"))
    print("enter elements separated by spaces")

    arr=list(map(int,input().split()))
    if len(arr)!=n:
        print("please enter exact no of elements that are sepcified")
        exit(0)

    quickSort(arr,0,n-1)
    print(arr)