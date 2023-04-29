import numpy as np
import re
import matplotlib.pyplot as plt


fig1 = plt.figure()
x = [1,2,3,4]
y = [2,4,6,8]

plt.plot(x,y, 'r.--', label='2x')
plt.title("My first graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")

x2 = np.arange(0, 4, 0.5)

plt.plot(x2[:5],x2[:5]**2, 'b', label='x^2')
plt.plot(x2[4:],x2[4:]**2, 'b--')
plt.legend()

fig2 = plt.figure()
labels = ['1st', '2nd', '3rd']
values = [8, 6, 3]
bars = plt.bar(labels,values)
bars[0].set_hatch('/')

plt.show()