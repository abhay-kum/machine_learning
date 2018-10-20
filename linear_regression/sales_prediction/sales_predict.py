import pandas as pd
import numpy as np
from numpy.linalg import inv

#new modified dataset using train_datset.csv
df_x=pd.read_csv("/data/trainnew.csv")

#the tota_sales_actual columns
df_y=pd.read_csv("/data/train_y.csv")

#test file columns containg same features as the train dataset
test_x=pd.read_csv("/data/testnew.csv")


#transpose  the x_train dataset
x_trans=df_x.transpose()

#multiplication of x_transponse and x_train dataset
a=np.matmul(x_trans,df_x)
#find the inverse of the multiplication
b=inv(a)
#multiplication of inverse and x_transpose
c=np.matmul(b,x_trans)
#multiplication of x_transpose and y_actual sales
d=np.matmul(c,df_y)

#assign matrix of zero values (1,255) 
y_test=np.zeros((255,1))

#convert array into matrix
y_test=np.matrix(y_test)

#print(np.shape(y_test))
x=np.matrix(test_x)
#x_features assign as matrix
i=0
# finding the prediction of total actual sales
for i in range(0,255):
    x_test=x[i,]
    x_test=np.matrix(x_test)
    predict=np.matmul(x_test,d)
    y=np.abs(predict)
    y_test[i]=np.round(y)
#print(y_test)
# save the predicted sales as text.csv
np.savetxt('text.csv', y_test, delimiter=',')
#np.to_csv("text.csv")
