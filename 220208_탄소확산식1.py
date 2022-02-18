import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci


t1=1
D=40
xmin=0
xmax=100
resolution=1000
x=np.linspace(xmin,xmax,resolution)
y1=1-sci.erf(x/((4*D*t1)**(1/2)))
t2=2
y2=1-sci.erf(x/((4*D*t2)**(1/2)))
t3=3
y3=1-sci.erf(x/((4*D*t3)**(1/2)))
t4=4
y4=1-sci.erf(x/((4*D*t4)**(1/2)))
t5=5
y5=1-sci.erf(x/((4*D*t5)**(1/2)))


fig = plt.figure(dpi=300)
fig,ax=plt.subplots()

ax.plot(x,y1)
ax.plot(x,y2)
ax.plot(x,y3)
ax.plot(x,y4)
ax.plot(x,y5)

fontname={'fontname':'Franklin Gothic Medium'}
fontname1 = {'fontname':'Times New Roman'}
plt.xlabel("x",fontsize=11,**fontname1)
plt.ylabel("C",fontsize=11,**fontname1)

plt.legend(["t=1","t=2","t=3","t=4","t=5"],loc="upper right",fontsize=8)

plt.ylim([0,1])

