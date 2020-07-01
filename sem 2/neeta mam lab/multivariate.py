import numpy as np
import matplotlib as mlt
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#
#def gauss(x,no_of_features,no_of_samples):    
#    temp=np.transpose(x)
#    print("gere",temp)
#    covariance=np.cov(x)
#    meu=[np.average(x) for i in x]
#    #print("x-meu",x-meu)
#    detemrninat= np.linalg.det(covariance)
#    #print((x-meu).shape)
#    #print(np.transpose(x-meu).shape)
#    #print(np.linalg.inv(covariance).shape)
#    print(meu)
#    print(covariance)
#    temp=-(1/2)*np.matmul(np.matmul(np.transpose((x-meu)[0]),np.linalg.inv(covariance)),(x-meu)[0])
#    p_c=(1/(((2*math.pi)**no_of_features)*detemrninat))*math.exp(temp)
#    return (p_c)
#
#no_of_samples=1
#no_of_features=2
#x_list=[]
#z_list=[]
#for i in range(no_of_samples):
#    x=np.random.rand(no_of_features,1)
#    x_list.append(x)
#	#print(x.shape,"here")
#    z=gauss(x,no_of_features,no_of_samples)
#	#print(x.shape)
#	#x_list.append(x.reshape(1,no_of_features)[0])
#    z_list.append(z)
#
#print(x_list)
#print(z_list)
#
#
#

#

def gauss(x,meu,e):
    #print("here")
    #print(x)
    #print(meu)
    #print(e)
    temp=(1/(((2*math.pi)**2)*np.linalg.det(e)))
    print(temp)
    t=math.exp( np.matmul( np.matmul(np.transpose(x-meu),np.linalg.inv(e)),(x-meu))/2)
    #print("output",temp*t)
    return temp*t
    



#features=np.random.rand(1000,2)
no=10
temp_x=np.linspace(0,1,no)
temp_y=np.linspace(0,1,no)
print(temp_x)
features=np.meshgrid(temp_x,temp_y)
#print(features.shape)
meu_x=0
for i in features:
    meu_x+=i[0]
meu_x/=no

#print(meu_x)


meu_y=0
for i in features:
    meu_y+=i[0]
meu_y/=no

#print(meu_y)
meu=np.array([meu_x,meu_y])
#print(meu)
temp=np.transpose(features)
e_list=[]
print(temp)

e=np.cov(temp)
print(e)
for i in features:
    e_list.append(gauss(i,meu,e))
print(features)
print(e_list)




fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[i[0] for i in x_list]
y =[i[0] for i in x_list]
z =e_list



ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
