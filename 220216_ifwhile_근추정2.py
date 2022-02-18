import matplotlib.pyplot as plt
import numpy as np

def g(x):
    #return sci.erf(x)-0.5
    #return np.log(x)-0.5
    return x*np.log(x)-0.5
    #return x*(x-1)*(x-2)

def instant_plot(xl0,xr0,xl,xr):
    xmin=xl0
    xmax=xr0
    resolution=100
    x=np.linspace(xmin,xmax,resolution)
    y=g(x)
    plt.plot(x,y,color='k')
    plt.axvline(x=xl,color='b')
    plt.axhline(y=0,color='k')
    plt.axvline(x=xr,color='r')
    plt.xlabel('x')
    plt.ylabel('g')
    plt.show()
    del xmin
    del xmax
    del resolution
    del x
    del y

xl0=0.1
xr0=5
tolerance=10**(-6)
xl=xl0
xr=xr0

if (g(xl)*g(xr)<0):
    xn=(xl+xr)/2
    if (g(xr)*g(xn))<=0:
        xl=xn
        instant_plot(xl0,xr0,xl,xr)
    else :
        xr=xn
        instant_plot(xl0,xr0,xl,xr)
    while (np.fabs(xl-xr)>=tolerance):
        xn=(xl+xr)/2
        if g(xr)*g(xn)<=0:
            xl=xn
            instant_plot(xl0,xr0,xl,xr)
        else :
            xr=xn
            instant_plot(xl0,xr0,xl,xr)
        xR=xl
        print(xR)

    
else :
    print("Try other xl and xr")
    
