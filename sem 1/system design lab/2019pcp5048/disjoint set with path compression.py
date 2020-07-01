class node:

     def __init__(self,x):
         self.val=x
         self.p=self
         self.rank=0


def link(x,y):
    if x.rank>y.rank:
        y.p=x
    else:
        x.p=y
    if x.rank==y.rank:
        y.rank+=1

def find_set(x):
    if x!=x.p:
        x.p=find_set(x.p)
    return x.p

def union(x,y):
    link(find_set(x),find_set(y))


a=node('a')
b=node('b')
c=node('c')
d=node('d')
e=node('e')
union(a,b)
union(c,d)
union(c,e)
union(a,e)

print(find_set(a).val)
print(find_set(b).val)
print(find_set(c).val)

