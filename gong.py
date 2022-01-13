import matplotlib.pyplot as plt
import numpy as np

filename = '//wsl$/Ubuntu/home/uni/going/testrepo/single_crystal_test_out.csv'
data = np.genfromtxt(filename,dtype=float,delimiter=',',names=True)
print(data['time'])
