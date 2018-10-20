import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from numpy.linalg import inv


x1=np.array([1,2,3,6])
y1=np.array([1,4,9,36])

#a=np.array([[1,1],[1,4],[1,3],[1,5]] )
a=np.array([[1,1,1],[1,2,4],[1,3,9],[1,6,36]])
b=a.transpose()
c=np.matmul(b,a)
d=inv(c)
e=np.matmul(d,b)
y=np.array([[1],[4],[9],[36]])
f=np.matmul(e,y)
print(f)
c=f[0]
b=f[1]
a3=f[2]
plt.scatter(x1,y1)
plt.plot(x1,x1*x1*a3+x1*b+c,'r')
plt.show()

## testing data :
x_test1=np.array([4,5])
y_test=np.array([])

y_test[0]=a*x_test1[0]*x_test1[0] +b*x_test1[0] +c

y_test[0]=a*x_test1[1]*x_test1[1] +b*x_test1[1] +c

x=x1+x_test1
y=y1 + y1_test

plt.scatter(x,y)
plt.plot(x,y,'r')
plt.show()
#X = np.array([1, 2, 3, 4, 5, 6, 7])
#Y = np.array([1.1,1.9,3.0,4.1,5.2,5.8,7])

#scatter (X,Y)
#slope, intercept = np.polyfit(X, Y, 1)
#plot(X, X*slope + intercept, 'r')
