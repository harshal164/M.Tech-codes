import math


text1=input()
text2=input()
dict1={}
dict2={}

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
for i in text1.split():
    if dict1.get(i):
        dict1[i]+=1
    else:
        dict1[i]=1

for i in text2.split():
    if dict2.get(i):
        dict2[i]+=1
    else:
        dict2[i]=1


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
print(vec1,vec2)
cosine_sim(vec1,vec2)