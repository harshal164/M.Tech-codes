import re,copy



# second_copy=copy.deepcopy



def literal_function():
    global  literals,constants
    samle_const=[]
    for i in constants:
        samle_const.extend(i.split(' '))
    print(samle_const)
    f1=open('keywords')
    keywords=list(f1.read().split('\n'))
    f=open('sample_c_input_for_2')
    data=f.read()

    words=re.findall(r"[\w']+", data)
    for i in words:
        if i not  in keywords and i not in constants:
            literals.append(i)
    print(literals)

    return






if __name__=="__main__":
    f = open("sample_c_input_for_2")
    text = list(f.read())
    flag = 0
    constants = []
    temp = []
    prev = 0
    literals = []
    for i in text:
        if i == '\n':
            text.remove('\n')

        if flag == 0:
            if ((i == '"' or i == "'")):
                flag = 1
                continue
            if (str.isnumeric(i)):
                temp.append(i)
                flag = 1
                prev = 1

        else:
            if (i != '"' or i != "'"):
                temp.append(i)
            if (i == '"' or i == "'"):
                constants.append(''.join(temp[:len(temp) - 1]))
                temp = []
                flag = 0
            if ((i == " " or i == ";" or i == ",") and prev == 1):
                prev = 0
                constants.append(''.join(temp[:len(temp) - 1]))
                temp = []
                flag = 0
    # print(text)

    print(constants)
    print(literals)

    literal_function()
