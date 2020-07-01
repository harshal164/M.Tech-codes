a=list(map(int,input().split()))
print(a)
for i in range(1,len(a)):
    temp=i
    while a[temp]<a[temp-1] and temp>0:
        a[temp],a[temp-1]=a[temp-1],a[temp]
        temp-=1
print(a)


    
