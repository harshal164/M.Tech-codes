import math
import numpy as np


def something(t):
    f=open(t)
    # print(f.readlines())

    l=f.readlines()
    # l=text.split()
    # print(l)
    final=[]
    for i in l:
        # print(i)
        temp=[]
        flag=0
        for j in i:
            if j=='"':
                if not flag:
                    flag=1
                else:
                    flag=0
                    temp.append('"')
                    final.append(''.join(temp))
                    temp=[]

            if not flag:
                if j.isalpha():
                    temp.append(j)
                else: 
                    if j in ['\n',',','?',' ','.']:
                        final.append(''.join(temp))
                        temp=[]
            else:
                temp.append(j)

                
            
        
        final.append(''.join(temp))
    # print(final)
    d={}
    s=set(final)
    for i in s:
        d[i]=final.count(i)
    del d['']
    print(d)
    return d



dict1=something('cc.txt')
dict2=something('fb.txt')
dic3=something('diego.txt')

# text1=input()
# text2=input()
# dict1={}
# dict2={}

def mahalanobis(vec1,vec2):
    inverse=(np.linalg.inv(np.cov(vec1,vec2)))




def minkowiski(vec1,vec2,p=3):
    output=0
    for i in range(len(vec1)):
        output+=(abs(vec1[i]-vec2[i]))**p
    output=output**(1/p)
    print("minkowiski",output)



def manhattan(vec1,vec2):
    output=0
    for i in range(len(vec1)):
        output+=abs(vec1[i]-vec2[i])
    print("manhattan distance",output)
def euclidian(vec1,vec2):
    output=0
    for i in range(len(vec1)):
        output+=(vec1[i]-vec2[i])**2
    output=math.sqrt(output)
    print("euclidian distance",output)


def cosine_sim(vec1,vec2):
    temp=0
    for i in range(len(vec1)):
        temp+=vec1[i]*vec2[i]
    t=0
    for i in vec1:
        t+=i**2
    t=math.sqrt(t)
    temp=temp/t
    t=0
    for i in vec2:
        t+=i**2
    t=math.sqrt(t)
    temp=temp/t
    print("cosine similarity",temp)
# for i in text1.split():
#     if dict1.get(i):
#         dict1[i]+=1
#     else:
#         dict1[i]=1

# for i in text2.split():
#     if dict2.get(i):
#         dict2[i]+=1
#     else:
#         dict2[i]=1


total_words=[]
print(dict1.keys())
for i in dict1.keys():
    total_words.append(i)
for i in dict2.keys():
    total_words.append(i)
total_words=set(total_words)
print(total_words)
for i in total_words:
    if not dict1.get(i,0):
        dict1[i]=0
    if not dict2.get(i,0):
        dict2[i]=0
print(dict1,dict2)

vec1=[]
vec2=[]
for i in total_words:
    vec1.append(dict1[i])
    vec2.append(dict2[i])
# print(vec1,vec2)

print("distance of cc and fb::::")
cosine_sim(vec1,vec2)
euclidian(vec1,vec2)
manhattan(vec1,vec2)
minkowiski(vec1,vec2)
mahalanobis(vec1,vec2)

