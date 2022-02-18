import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci


D=40
tmin=0
tmax=100
resolution=1000
t=np.linspace(tmin,tmax,resolution)


x=0.4769*(4*D*t)**(1/2)

fig = plt.figure(dpi=300)
fig,ax=plt.subplots()

t1=t**(1/2)
ax.plot(t1,x)



fontname={'fontname':'Franklin Gothic Medium'}
fontname1 = {'fontname':'Times New Roman'}
plt.xlabel("t",fontsize=11,**fontname1)
plt.ylabel("x",fontsize=11,**fontname1)





