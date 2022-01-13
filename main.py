import matplotlib.pyplot as plt
import numpy as np

filename = '//wsl$/Ubuntu/home/uni/going/testrepo/single_crystal_test_out.csv'
data = np.genfromtxt(filename,dtype=float,delimiter=',',names=True)
# print(data['time'])
# print(data['e_zz'])
# print(data['stress_zz'])
x=data['e_zz']
y=data['stress_zz']
fig = plt.figure(dpi=300)
fig,ax=plt.subplots()
ax.plot(x,y)
plt.show()
fig.savefig('figure220113.png',format='png',bbox_inches='tight')


