import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import scipy.special as sci

def find_neardata(X,x,y):
    for i in range(x.size-1):
        if (x[i]<=X):
            x1=x[i]
            x2=x[i+1]
            y1=y[i]
            y2=y[i+1]
    return x1,x2,y1,y2

def ya(X,x,y):
    x1,x2,y1,y2=find_neardata(X,x,y)
    slop=(y2-y1)/(x2-x1)
    distance=X-x1
    return y1+slop*distance

def instant_plot(xl0,xr0,xl,xr,xd,yd):
    plt.plot(xd,yd,color='k')
    plt.axvline(x=xl,color='b')
    plt.axhline(y=0,color='k')
    plt.axvline(x=xr,color='r')
    plt.xlabel('x')
    plt.ylabel('g')
    plt.show()
    #del x
    #del y

xl0=-1
xr0=10
tolerance=10**(-6)
xl=xl0
xr=xr0

xd=np.genfromtxt('xc.txt',dtype='float',delimiter='')
yd=np.genfromtxt('yc.txt',dtype='float',delimiter='')

xmin=min(xd)
xmax=max(xd)

if (xmin<=xl and xmax>=xr):
    if (ya(xl,xd,yd)*ya(xr,xd,yd)<=0):
        xn=(xl+xr)/2
    if (ya(xr,xd,yd)*ya(xn,xd,yd)<=0):
        xl=xn
        #instant_plot(xl0,xr0,xl,xr)
        instant_plot(xl0,xr0,xl,xr,xd,yd)
    else :
        xr=xn
        #instant_plot(xl0,xr0,xl,xr)
        instant_plot(xl0,xr0,xl,xr,xd,yd)
    while (np.fabs(xl-xr)>=tolerance):
        xn=(xl+xr)/2
        if (ya(xr,xd,yd)*ya(xn,xd,yd)<=0):
            xl=xn
            #instant_plot(xl0,xr0,xl,xr)
            instant_plot(xl0,xr0,xl,xr,xd,yd)
        else :
            xr=xn
            #instant_plot(xl0,xr0,xl,xr)
            instant_plot(xl0,xr0,xl,xr,xd,yd)
        xR=xl
        #print(xR)
        #f=ya(1.2,xd,yd)
        print(xR)
        
else :
    print("Try other xl and xr")