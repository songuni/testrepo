import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl



xmin=-1
xmax=1
resolution=500
x=np.linspace(xmin,xmax,resolution)
ymin=-1
ymax=1
resolution=500
y=np.linspace(ymin,ymax,resolution)
#print(x)
#print(y)
#print(x.ndim)
#print(x.size)

cm=1/2.54

fig = plt.figure(dpi=1000)
fig,ax=plt.subplots(figsize=(14*cm,9*cm))

X,Y=np.meshgrid(x,y)
#print(X.ndim)
#print(Y.ndim)

f=np.sin(np.pi*X)*np.cos(np.pi*Y)

extent=[min(x),max(x),min(y),max(y)]


im=plt.imshow(f,extent=extent,
          cmap=plt.cm.RdBu)

fig.savefig('220209.png',format='png',bbox_inches='tight',dpi=1000)

