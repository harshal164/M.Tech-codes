
def c1_set(dataset):
    c_1=[]
    for d in dataset:
        for i in d:
            if [i] not in c_1:
                c_1.append([i])
    c_1.sort()
    return list(map(set,c_1))

def ck_set(l_k, k):
    c_k=[]
    for i in range(len(l_k)):
        for j in range(i+1,len(l_k)):
            l_1 = list(l_k[i])[:k-2]
            l_2 = list(l_k[j])[:k-2]
            if(l_1==l_2):
                c_k.append(l_k[i] | l_k[j]) 
    return c_k



def makeL_k(data, c_k, min_sup):
    L_k=[]
    for i in c_k:
        score=0
        num_items = float(len(data))
        data=list(map(set,data))
        for t in data:
            if i.issubset(t):
                score+=1
        support = score/num_items
        if support >= min_sup:
            L_k.append(i)

    return L_k



def apriori_algorithm(dataset, min_sup):
    c_1 = c1_set(dataset)
    l_1 = makeL_k(dataset, c_1, min_sup)
    #print("C1: ",C1)
    print("L1:",l_1)
    L = [l_1]
    k=2
    while(len(L[k-2])>0):
        c_k = ck_set(L[k-2], k)
        l_k = makeL_k(dataset, c_k, min_sup)
        #print("C{}: {}".format(k,Ck))
        print("L{}: {}".format(k,l_k))
        L.append(l_k)
        k+=1
    return L[:-1]

f=open("sample_apriori")
temp=[]
#for i in f:    
    #temp.append((f.read()))
#print(temp[0].split("\n"))
temp=f.readlines()
print(list(temp))
inp=[]
for i in temp:
    n=i.split(",")
    n[-1]=n[-1][:-1]
    n=list(map(int,n))
    inp.append(n)
print(inp)
#while temp.find("\n"):
#    print(temp[:temp.index("\n")])
#    temp=temp[temp.index("\n")+1:]

minsup=0.2
L=apriori_algorithm(inp,minsup)
print("L: ",L)
print("Itemset: ",L[-1])
