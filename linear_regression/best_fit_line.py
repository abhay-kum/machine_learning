import matplotlib.pyplot as plt
import numpy as np
#from sklearn import datasets, linear_model
from numpy.linalg import inv


a1=np.array([1,4,3,5])
b1=np.array([1,5,2,6])
a=np.array([[1,1],[1,4],[1,3],[1,5]] )
b=a.transpose()
c=np.matmul(b,a)
d=inv(c)
e=np.matmul(d,b)
y=np.array([[2],[5],[2],[6]])
f=np.matmul(e,y)
print(f)
c=f[0]
m=f[1]
plt.scatter(a1,b1)
plt.plot(a1,a1*m+c,'r')
plt.show()

#X = np.array([1, 2, 3, 4, 5, 6, 7])
#Y = np.array([1.1,1.9,3.0,4.1,5.2,5.8,7])

#scatter (X,Y)
#slope, intercept = np.polyfit(X, Y, 1)
#plot(X, X*slope + intercept, 'r')
