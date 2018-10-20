
from sklearn import datasets
dataset = datasets.load_digits()



import numpy as np

import matplotlib.pyplot as plt
imgc = np.zeros((64,1797))

n_sample = len(dataset.images)
data = dataset.images.reshape(n_sample,-1)

dist = np.zeros(1797)
darray= np.zeros(1797)
sa = np.zeros(1797)

for i in range(0,1797):
    dist[i] = np.sqrt(np.sum(( data[1000]- data[i]) ** 2))  
    
    
darray = np.array(dist)

sa = sorted(darray)
k=10
for i in range(0,k):
    for j in range(0,1797):
        if(sa[i+1] == dist[j]):
            print(dataset.target[j])
            
            
plt.figure(1, figsize=(3, 3))
plt.imshow(dataset.images[0], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
