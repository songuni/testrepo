#220128 레전드에 수학함수 넣기 , 그래프 사이즈 및 해상도 설정, 플롯 설정

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci


xmin=0
xmax=1
resolution=1000
x=np.linspace(xmin,xmax,resolution)
#print(x)
y=x**2
#print(y)
y2=np.sin(2*np.pi*x)
y3=np.cos(2*np.pi*x)
y4=x*np.log(x)+(1-x)*np.log(1-x)
y5=np.e**(-x**2)
y6=1+np.tanh((x-0.5)/0.01)
y7=sci.erf(x)

cm=1/2.54

fig = plt.figure(dpi=1000)
fig,ax=plt.subplots(figsize=(14*cm,9*cm))

ax.plot(x,y,color='#1f77b4', marker='4', linestyle='--', linewidth=1, markersize=7, markevery=100)
ax.plot(x,y2,color='#7f7f7f',marker='*', linestyle='-', linewidth=1, markersize=7, markevery=100)
ax.plot(x,y3,color='#ff7f0e',marker='8', linestyle='-.', linewidth=1, markersize=7, markevery=200)
ax.plot(x,y4,color='#2ca02c',linestyle=':', linewidth=1)
ax.plot(x,y5,color='#d62728', linewidth=2)
ax.plot(x,y6,color='#9467bd',marker='<', linestyle=':', linewidth=1, markersize=7, markevery=200)
ax.plot(x,y7,color='#8c564b')

fontname={'fontname':'Franklin Gothic Medium'}
fontname1 = {'fontname':'Times New Roman'}
plt.xlabel("x",fontsize=11,**fontname1)
plt.ylabel("y",fontsize=11,**fontname1)
plt.legend([r'$y1=x^{2}$', r'y2=sin(2 $\pi x$)',r'y3=cos(2 $\pi x$)',r'y4=xln(x)+(1-x)ln(1-x)', r'$y5=e^{-x^{2}}$',
            r'y6=$\frac{1}{2}$+$\frac{1}{2}$ tanh$(\frac{x-0.5}{0.01})$',r'y7=erf(x)'],loc="upper left",fontsize=7,ncol=2)





plt.xticks(np.arange(min(x),max(x),0.1),fontsize=10,**fontname1)
plt.yticks(np.arange(-3,5,0.5),fontsize=10,**fontname1)
plt.title("[ x-y Graph ]",fontsize=18,**fontname)

plt.ylim([-1,4])

fig.savefig('수학함수연습_220128.png',format='png',bbox_inches='tight',dpi=1000)
