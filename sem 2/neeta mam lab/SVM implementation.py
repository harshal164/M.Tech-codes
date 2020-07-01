



import numpy as np

from sympy import *



x=np.array([[-1,-1],[1,1],[-1,1],[1,-1]])
y=np.array([1,1,-1,-1])
x1=symbols('x1')
x2=symbols('x2')

def Q_fun(lambda_list):
    result=sum(lambda_list)
    for i in range(len(x)):
        for j in range(len(x)):
            result-=1/2*lambda_list[i]*lambda_list[j]*y[i]*y[j]*k_mat[i][j]
    return result         

def L_fun(lambda_list,meu):
    return Q_fun(lambda_list)+meu*(np.dot(lambda_list,y))


def L_differentiate(L_instance):
    op=[]
    for i in range(len(y)):
        op.append(L_instance.diff(symbols('lambda'+str(i))))
    op.append(L_instance.diff(symbols('meu')))
    return op
    
    
def solve_lin_que(x):
    A=[]
    
    A=solve((x[0],x[1],x[2],x[3],x[4]),(symbols('lambda0'),symbols('lambda1'),symbols('lambda2'),symbols('lambda3'),symbols('meu')))
    return A


def phi(x):
    return np.array([1,np.sqrt(3)*x[0],np.sqrt(3)*x[1],np.sqrt(3)*x[0]**2,np.sqrt(3)*x[1]**2,np.sqrt(6)*x[0]*x[1],x[0]**3,x[1]**3,np.sqrt(3)*x[0]*x[1]**2,np.sqrt(3)*x[0]*x[0]*x[1]])


def K(phi_x,phi_xi):
    return np.matmul(phi_x.T,phi_xi)


phi_x=[phi(i) for i in x]    
k_mat=[]
for i in range(len(x)):
    temp=[]
    for j in range(len(x)):
        temp.append(K(phi_x[i],phi_x[j]))
    k_mat.append(temp)




lambda_list=[symbols('lambda'+str(i)) for i in range(len(y))]

meu=symbols('meu')

L_instance=L_fun(lambda_list,meu)
L_diff=L_differentiate(L_instance)

unknown_param_vals=solve_lin_que(L_diff)


w0=0
for i in range(len(y)):
    w0+=unknown_param_vals[symbols('lambda'+str(i))]*y[i]*phi_x[i]
    
#optimal hyperplane


phi_placeholder=np.array([1,np.sqrt(3)*x1,np.sqrt(3)*x2,np.sqrt(3)*x1**2,np.sqrt(3)*x2**2,np.sqrt(6)*x1*x2,x1**3,x2**3,np.sqrt(3)*x1*x2**2,np.sqrt(3)*x1*x1*x2])


hyperplane=np.dot(w0.T,phi_placeholder)
print("optimal hyperplane is ",hyperplane,"=0")
