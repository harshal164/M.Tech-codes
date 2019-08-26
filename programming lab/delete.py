import sys
import string
delim=['\t','\n',',',';','(',')','{','}','[',']','#','<','>',' ']
oper=['+','-','*','/','%','=','!']
lines=[]
with  open("sample_c_input_for_2") as f:
    lines=f.readlines()
print(lines)
token=[]
flag=0
for i in lines:
    temp = []
    p=0
    for j in i:

        if ((j not in delim and j not in oper) or flag):
            if j=="\\":
                p=1
            if j=='"' and p:
                p=0
                continue
            if j=='"':
                flag=not flag
            temp.append(j)
        else:
            temp=''.join(temp)
            token.append(temp)
            temp=[]
                # temp.append(j)
        # te
    # print(''.join(temp))
print(token)
        # if token.get(temp):
        #     token[temp]=token.get(temp)+1
        # else:
        #     token[j]=1
# print(token)