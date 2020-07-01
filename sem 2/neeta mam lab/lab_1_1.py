import matplotlib.pyplot as plt
import numpy as np
import random
gen_dist=[]
imp_dist=[]
x=[]
res=[]
for i in range(100):
    x.append(random.random())
    
for i in x:
    gen_dist.append(3+4*i*i)
    imp_dist.append(5-4*i*i)
    print("x= ",i, "genuine = ",3+4*i*i, " imposter= ",5-4*i*i)
plt.plot(x,gen_dist,'ro')
plt.plot(x,imp_dist,'bo')





def something():
    tp=[]
    tn=[]
    fp=[]
    fn=[]
    
    for i in range(10):
        predicted=[]
        temp=[]
        for j in x:

            if j<i:
                predicted=1
            else:
                predicted=0
        

        

# plt.show()