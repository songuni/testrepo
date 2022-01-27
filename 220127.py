import matplotlib.pyplot as plt
import numpy as np

filename = '//wsl$/Ubuntu/home/uni/going/testrepo/single_crystal_test_out.csv'
data = np.genfromtxt(filename,dtype=float,delimiter=',',names=True)
# print(data['time'])

x=data['e_zz']
y=data['stress_zz']
y2=data['pk2']
fig = plt.figure(dpi=300)
fig,ax=plt.subplots()
ax.plot(x,y)
ax.plot(x,y2)
fontname={'fontname':'Impact'}
fontname1 = {'fontname':'Times New Roman'}
plt.xlabel("strain",fontsize=20,**fontname1)
plt.ylabel("stress",fontsize=20,**fontname1)
plt.xticks(np.arange(min(x),max(x),0.001),fontsize=16,**fontname1)
plt.yticks(np.arange(min(y),max(y),5),fontsize=16,**fontname1)
plt.legend(["stress_zz","pk2"])
plt.xlim([0.002,0.005])
plt.ylim([120,max(y)])
plt.title("strain-stress",fontsize=22,**fontname)


plt.show()
fig.savefig('figure220113.png',format='png',bbox_inches='tight')



