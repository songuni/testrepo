#조건문 : if(), elif, else
#판별문 : 참? 거짓?
#반복문 : while(), for() 

#목표 : 함수의 근을 찾는 코드 작성
#알고리즘 : 이분법(bisection method)

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import scipy.special as sci

def g(x):
    #return sci.erf(x)-0.5
    #return np.sin(x)-0.75
    #return np.log(x)-0.5
    #return x*np.log(x)-0.5
    return x*(x-1)*(x-2)
    #return x*0-5

def instant_plot(xl0,xr0,xl,xr):
    xmin=xl0
    xmax=xr0
    resolution=100
    x=np.linspace(xmin,xmax,resolution)
    y=g(x)
    plt.plot(x,y,color='k')
    plt.axhline(y=0,color='k')
    plt.axvline(x=xl,color='b')
    plt.axvline(x=xr,color='r')
    plt.xlabel('x')
    plt.ylabel('g')
    plt.show()
    del xmin
    del xmax
    del resolution
    del x
    del y
    
xl0=-1
xr0=3
xl=xl0
xr=xr0
    
tolerance=1e-6

instant_plot(xl0,xr0,xl,xr)

if(g(xl)*g(xr)>0):
    print('No root between',xl,xr)
    instant_plot(xl0,xr0,xl,xr)
else:
    print('Root is here')
    xc=(xl+xr)/2
    gc=g(xc)
    
    if (g(xl)*g(xc)<=0):
        xr=xc
    else:
        xl=xc
    #print(np.fabs(xr-xl)<tolerance)
     #수렴판정
    instant_plot(xl0,xr0,xl,xr)
    
    while(np.fabs(xr-xl)>tolerance):
        print('Root is here')
        xc=(xl+xr)/2
        gc=g(xc)
        if (g(xl)*g(xc)<=0):
            xr=xc
        else:
            xl=xc
        xa=xl
        instant_plot(xl0,xr0,xl,xr)
        
        #print(np.fabs(xr-xl)<tolerance)
        print(xa) 

