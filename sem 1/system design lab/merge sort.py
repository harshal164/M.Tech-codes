def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0


        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1


        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__=='__main__':
    n = int(input("enter no of elements in list"))
    print("enter elements separated by spaces")

    arr = list(map(int, input().split()))
    if len(arr) != n:
        print("please enter exact no of elements that are specified")
        exit(0)
    mergeSort(arr)

    print(arr)