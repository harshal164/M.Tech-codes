import copy
elements=[]
rules={}
count=1

f=open('sample_for_cfg')
t=list(f.read())
# print(list(t.strip('\n')))
length=len(t)
for i in range(length):
    if '\n' in t:
        ind=t.index('\n')
        lhs=t[:t.index(' ')]
        lhs=''.join(lhs)
        rhs=t[(t.index(' ')+1):ind]
        rhs=''.join(rhs)
        rules.setdefault(lhs, []).append(rhs)
        for j in lhs:
            if j!='e' and j not  in elements:
                    elements.append(j)

            for j in rhs:
                if j!='e' and j not in elements:
                    elements.append(j)
        i=ind
        t=t[(ind+1):]

lhs=t[:t.index(' ')]
lhs=''.join(lhs)
rhs=t[(t.index(' ')+1):ind]
rhs=''.join(rhs)
rules.setdefault(lhs, []).append(rhs)

    # print(t.remove('\n'))
print(rules)

def replace_by_nonterminal(small_dict):
    # print("inverse dictionary for terminals:" ,small_dict)

    global rules,elements
    print(rules)
    new_dict=copy.deepcopy(rules)
    indexof=0
    for key, value in new_dict.items():
        for i in value:
            if str.islower(i) and len(i)>1:
                print(i)
                indexof =rules[key].index(i)
                rules[key].remove(i)

                # print("rules after removal",rules)
                i=list(i)
                temp=[]
                for k in i:
                    print(small_dict.get(k))
                    temp.append(small_dict[k])
                i=''.join(temp)
                rules[key].insert(indexof,i)
            # print("rules after insertion",rules)




def break_terminal():
    global count, rules, elements
    # print(dict(zip(elements, elements)))
    new_dict=copy.deepcopy(rules)
    small_elements=[x for x in elements if str.islower(x)]
    count1=65
    small_dict=dict(zip(small_elements,small_elements))
    for key in small_dict:
        if small_dict[key].islower():
            while (chr(count1) in elements):
                count1 += 1
            small_dict[key]=chr(count1)
            # rules[chr(count1)]=key
            rules.setdefault(chr(count1), []).append(key)
            count1+=1
    replace_by_nonterminal(small_dict)


def remove_large_production():

    global count,rules,elements
    new_dict = copy.deepcopy(rules)
    for key in new_dict:
        values = new_dict[key]
        for i in range(len(values)):
            if len(values[i]) > 2:

                for j in range(0, len(values[i]) - 2):
                    if j == 0:
                        rules[key][i] = rules[key][i][0] + "N" + str(count)
                    else:
                        # print(values[i][j] + "N" + str(count))
                        rules.setdefault(new_key, []).append(values[i][j] + "N" + str(count))
                        # count += 1
                    elements.append("N" + str(count))

                    new_key = copy.deepcopy("N" + str(count))
                    count += 1
                rules.setdefault(new_key, []).append(values[i][-2:])

    return rules, elements





def remove_empty_production():
    global rules,elements,count
    empty_list=[]
    new_dict = copy.deepcopy(rules)
    for key in new_dict:
        values = new_dict[key]
        for i in range(len(values)):

            if values[i] == 'e' and key not in empty_list:
                empty_list.append(key)

                rules[key].remove(values[i])

        if len(rules[key]) == 0:
            if key not in rules:
                elements.remove(key)
            rules.pop(key, None)

    new_dict = copy.deepcopy(rules)
    for key in new_dict:
        values = new_dict[key]
        for i in range(len(values)):
            if len(values[i]) == 2:

                if values[i][0] in empty_list and key != values[i][1]:
                    rules.setdefault(key, []).append(values[i][1])
                if values[i][1] in empty_list and key != values[i][0]:
                    if values[i][0] != values[i][1]:
                        rules.setdefault(key, []).append(values[i][0])
            else:
                for j in range(len(values[i])):
                    if values[i][j] in empty_list:
                        rules.setdefault(key,values[i:(j-1)]).append(values[i][(j+1):])

    return rules, elements







#
# n=int(input("enter no of production ruules:"))
# if n <= 2:
#     print('N must be a number >2!')
#     exit(0)
#
# print("enter production rules LHS and RHS separated by spaces and 'e' for null production ")
#
# for i in range(n):
#     lhs, rhs=(input("rule "+(str(i+1)+":")).split())
#
#
#     for j in lhs:
#         if j!='e' and j not  in elements:
#             elements.append(j)
#
#     for j in rhs:
#         if j!='e' and j not in elements:
#             elements.append(j)
#     rules.setdefault(lhs,[]).append(rhs)
#
#
#

print("after break terminal ")
break_terminal()
print(rules)


print("after large rule removal:")
remove_large_production()
print(rules)
# print(elements)


print("rules after empty rule removal")
remove_empty_production()
print(rules)
# print(elements)

for key,value in rules.items():
    for i in value:

        print(key,"->",i)
print(elements)