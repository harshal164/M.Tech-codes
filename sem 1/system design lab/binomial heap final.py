class Node:

    def __init__(self,data):
        self.data=data
        self.parent=None
        self.child=None
        self.sibling=None
        self.degree=0
head=[]
def union_tree():
    if (len(head)>1):
        i=0
        while i<len(head):
            x=head[i]
            if len(head)<=i+1:
                return
            next_x=head[i+1]

            if x.degree==next_x.degree:
                if x.data>=next_x.data:
                    temp=head.pop(i)
                    next_x.degree+=1
                    temp.parent=next_x
                    temp.sibling=next_x.child
                    next_x.child=temp
                    head.sort(key=lambda x: x.degree)

                else:
                    temp = head.pop(i+1)
                    x.degree += 1
                    temp.parent = x
                    temp.sibling = x.child
                    x.child = temp
                    head.sort(key=lambda x: x.degree)
            else:
                i += 1


            head.sort(key=lambda x:x.degree)

    return
def extract_min():
    min = 0
    for i in range(1,len(head)):
        if head[i].data <= head[min].data:
            min = i
    print("minimum value is",head[min].data)
    min=head[min]
    if min.child:
        temp=min.child
        while temp:
            temp.parent=None
            head.insert(0,temp)
            temp1=temp.sibling
            temp.sibling=None
            temp=temp1
    head.sort(key=lambda x: x.degree)
    head.remove(min)
    union_tree()
    # return head[min]
def insert_node(x):

    temp=Node(x)

    temp.degree=0
    head.insert(0,temp)
    union_tree()
    return
def print_tree(node):
    print(node.data)
    if node.degree >0:

        print_tree(node.child)
    if node.sibling:
        print_tree(node.sibling)
def get_min():
    min=head[0].data
    for i in head:
        if i.data<=min:
            min=i.data
    return min
if __name__=="__main__":
    print("##### sample heap for 0 to 12 #####" )
    for i in range(13):
        insert_node(i)

    #
    for i in head:
        print("for root as",i.data)
        print_tree(i)
    # for i in range(13):
    #     extract_min()
    extract_min()
    print("heap after extracting min value")
    for i in head:
        print("for root as", i.data)
        print_tree(i)
