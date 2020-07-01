# def partition(left,right,lis,mom):
#     pivot=left

def partition(arr,low,high):
    pos=0
    for i in range(low,high):
        if arr[0]>arr[i]:
            pos+=1
    arr[0],arr[pos]=arr[pos],arr[0]
    return pos

def change_mom_place(left,right,lis,mom):
    # print(lis[lis.index(mom)])
    temp=lis[0]
    t=lis.index(mom)
    lis[0]=lis[lis.index(mom)]
    lis[t]=temp
    # print(lis)
    # pass
lis=list(map(int,input().split()))
# print(lis)
k=int(input("enter kth calue to find max"))
k-=1
def find_mom(lis,k):
    second = []
    batch_size = 3
    for i in range(len(lis) // batch_size + 1):
        if i * batch_size < len(lis):
            if i * batch_size + batch_size < len(lis):
                temp = lis[i * batch_size:i * batch_size + batch_size]

            else:
                temp = lis[i * batch_size:]
            temp.sort()
            # print(temp)
            second.append(temp[len(temp) // 2])
    # print(second)

    second.sort()
    mom = second[len(second) // 2]
    # print(mom)
    return mom

mom=find_mom(lis,k)
change_mom_place(0,1,lis,mom)
correct_pos=(partition(lis,0,len(lis)-1))
while True:
    if correct_pos>k:
        lis=lis[:correct_pos]

        mom = find_mom(lis, k)
        change_mom_place(0, 1, lis, mom)
        correct_pos = (partition(lis, 0, len(lis) - 1))
    elif correct_pos<k:
        lis=lis[correct_pos+1:]

        mom = find_mom(lis, k)
        change_mom_place(0, 1, lis, mom)
        correct_pos = (partition(lis, 0, len(lis) - 1))
    else:
        print(lis[correct_pos])
        break
