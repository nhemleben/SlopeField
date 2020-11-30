

#uniform selection of functions?


import matplotlib.pyplot as plt
import turtle
import random
import numpy as np
from scipy import interpolate


def integrate_coefs(A):
    n = len(A)
    int_sum = 0
    for i in range(A):
        int_sum = int_sum + A[i]/(i+1)
    return int_sum

def const_interp( A , X):
    return integrate_coefs(A)
     
#vecotr of values of function at X points
def eval_poly( A , X):
    n = len(A)
    m - len(X)
    B=[]
    for j in range(m):
        x = X[j]
        b =0
        for i in range(n):
            b = b + pow(x,i) * A[i] 
        B.append(b)
    return B


def line_interp( B , X, X_Int):
    #evaluate at C, interp at points X, values B
    S = np.interp(X_Int , X, B)
    #need abs here?
    K = [abs(s) for s in S]
    return sum(K)/len(C)

def cubic_interp( B , X, X_Int):
    tck = interpolate.splrep(X, B, s=0)
    ynew = interpolate.splev(X_Int, tck, der=0)


def grab_coefs(L, N):
    A =[]
    for i in range(N):
        A.append( np.random.uniform(-L,L) )
    return A



Fid_Int = 100
N=10
X = np.arange(0,1,1/N)
X_Int = np.arange(0,1,1/Fid_Int)
A = [0,1]
B = eval_poly( A, X)
int_lin = line_interp( B, X, X_Int)
int_cube = cubic_interp( B, X, X_Int)








