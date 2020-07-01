import numpy as np
import matplotlib.pyplot as plt
w1 = [-1,3,-1,4,-1,5,-1,6,-1,7,-1,8,-2,9,-1,11,1,4,1,6,1,9,1,10,2,6,2,7,2,8,2,10,3,5,3,7,3,8,3,9,3,10,4,6,4,8,4,9,5,7,5,9,6,7,6,8]
w2 = [3,3,4,4,5,2,5,3,5,6,6,2,6,3,7,3,7,4,7,6,8,2,8,4,8,7,8,9,7,10,9,5,9,8,10,2,10,4,10,6,11,3,11,5,1,17,11,8,12,4,12,6,13,3,14,2,14,4,15,3]

cols = len(w1)/2
w1_ = np.reshape(np.array(w1),(cols,2,1))
cols = len(w2)/2
w2_ = np.reshape(np.array(w2),(cols,2,1))
for i,x in enumerate(w2_):
    print(x)
    if i > 5:
        break

w1__ = np.average(w1_, axis = 0)

print("w1__")
print(w1__)

w2__ = np.average(w2_, axis = 0)

print("w2__")
print(w2__)

u__ = np.average(np.array([w1__,w2__]),axis = 0)
print("u__")
print(u__)
print("w1_.shape")
print(w1_.shape)
print("w1__.shape")
print(w1__.shape)
z1 = w1_ - w1__
z2 = w2_ - w2__
y = np.matrix(z1)
S1 = np.matmul(y.T,y)
y = np.matrix(z2)
S2 = np.matmul(y.T,y)
Sw = S1 + S2
print("Sw")
print(Sw)

b1 = w1__ - u__
b2 = w1__ - u__
Sb1 = np.matmul(b1,b1.T)
Sb2 = np.matmul(b2,b2.T)
print("Sb1")
print(Sb1)
print("Sb2")
print(Sb2)
Sb = Sb1 + Sb2
print("Sb")
print(Sb)

Sw_1 = np.linalg.inv(Sw)
print("Sw_1")
print(Sw_1)

A = np.matmul(Sw_1,Sb)

lam, v = np.linalg.eig(A)

print("lam")
print(lam)
print("v")
print(v)

wstar = np.matmul(Sw_1,w1__ - w2__)
print("W*(proportional to v[0], the LDA projection axis):")
print(wstar)

wstar_hat = np.asarray(wstar)/np.linalg.norm(np.asarray(wstar))
print("w*_hat:")
print(wstar_hat)

w1_star = np.matmul(np.matrix(w1_), wstar_hat)
w2_star = np.matmul(np.matrix(w2_), wstar_hat)

print("Projected w1 class:")
print(w1_star)
print("Projected w2 class:")
print(w2_star)

for item in w1_:
    plt.plot(item[0],item[1],'ro',markersize=5)
for item in w2_:
    plt.plot(item[0],item[1],'bo',markersize=5)
xpoints = []
ypoints = []
for l in range(-1400,1400):
    xpoints.append(l*np.asarray(wstar)[0][0])
    ypoints.append(l*np.asarray(wstar)[1][0])
plt.plot(xpoints,ypoints,'k-',linewidth=0.7)

for item,k in zip(w1_star,w1_):
    i = np.asarray(item)[0][0]
    x = wstar_hat[0][0] * i
    y = wstar_hat[1][0] * i
    plt.plot([x,k[0]],[y,k[1]],'k--',linewidth=.4)
    plt.plot(x,y,'ro',markersize=4,markerfacecolor='none')

for item,k in zip(w2_star,w2_):
    i = np.asarray(item)[0][0]
    x = wstar_hat[0][0] * i
    y = wstar_hat[1][0] * i
    plt.plot([x,k[0]],[y,k[1]],'k--',linewidth=0.4)
    plt.plot(x,y,'bo',markersize=4,markerfacecolor='none')

plt.axis([-10,20,-10,20])
plt.show()
