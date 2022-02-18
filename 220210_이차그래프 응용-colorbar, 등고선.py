
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

f=Y

extent=[min(x),max(x),min(y),max(y)]

fontname={'fontname':'Franklin Gothic Medium'}
fontname1 = {'fontname':'Times New Roman'}
plt.xlabel("x",fontsize=11,**fontname1)
plt.ylabel("y",fontsize=11,**fontname1)

#im=plt.imshow(f,extent=extent, cmap=plt.cm.RdBu,origin='lower')
#origin을 안 넣었을 때 모니터 좌표값으로 그래프가 나타나기에 왼쪽 위가 영점으로 나옴

im=plt.pcolormesh(X,Y,f,shading='auto', cmap=plt.cm.RdBu)

ax.set_aspect('equal','box')
#그래프의 가로,세로가 똑같아지게 함.

ax.set(xlim=(-1,1),ylim=(-1,1))

plt.xticks(np.arange(-1,1+0.1,0.25),fontsize=10)
plt.yticks(np.arange(-1,1+0.1,0.25),fontsize=10)
#arange의 문제 뒷숫자가 끝까지 안 나옴으로 작은 수를 더해준다.

cset=plt.contour(X, Y ,f,np.arange(-1,1+0.1,0.5
                                     ),colors='k')

plt.clabel(cset,inline=True,fontsize=9)

plt.title(r'$f=y$',fontsize=18,**fontname)

colorbar=plt.colorbar(im)

colorbar.set_label('y',rotation=0)

#fig.savefig('220209.png',format='png',bbox_inches='tight',dpi=1000)