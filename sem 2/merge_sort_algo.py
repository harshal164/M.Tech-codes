def merge_sort(a,l,r):
    if l<r:
        mid=l+r//2
        l_half=a[:mid]
        r_half=a[mid:]
        merge_sort(a,l,mid)
        merge_sort(a,mid,r)
        



a=list(map(int,input().split()))
merge_sort(a,0,len(a)-1)