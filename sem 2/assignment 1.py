f=open('sample')
# print(f.readlines())

l=f.readlines()
# l=text.split()
# print(l)
final=[]
for i in l:
    print(i)
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
print(final)
d={}
s=set(final)
for i in s:
    d[i]=final.count(i)
del d['']
print(d)


