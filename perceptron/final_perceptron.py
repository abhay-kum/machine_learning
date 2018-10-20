import matplotlib.pyplot as plt
import numpy as np

def plotter (xdata,xcls,w):
    plt.figure()
    #note plotter works only for 2d
    #here i take the liberty to define the graph area from
    # -4 to 4 in both axis
    plt.axis([-4, 4, -4, 4])
    #we need some points on the line to show w, let them be wx2,wx1
    #to plot the predicted w let us find X1 by substituting X2
    wx1 = list([-4,4])
    if (w[2-2]!=0):
        wx2 = [(-((x*w[2-1])+w[2-0])/w[2-2]) for x in wx1 ] 
    else:
        wx2 = wx1
        wx1 = [-w[2-0]/w[2-1] for x in wx2]
    plt.plot(wx1,wx2)
    #now we need to plot the class of data
    x_data_c1 = np.zeros(0,dtype = float)
    x_data_c0 = x_data_c1
    
    for index in range(len(xcls)):
        if(xcls[index] == -1):
            x_data_c0 = np.append(x_data_c0,xdata[index],axis = 0)
        else:
            x_data_c1 = np.append(x_data_c1,xdata[index],axis = 0)
    
    #they are store continiously ex (0,0),(0,1) is stored as [0 0 0 1]
    plt.plot( x_data_c0[0::2] , x_data_c0[1::2],'ro' )
    plt.plot( x_data_c1[0::2] , x_data_c1[1::2],'go' )
    plt.show(block=False)
    plt.show
    return


#define your classifier ie sigmoid or just direct binary cls.
def classifier (inter):
    #simple binary classifier
    
    if (inter > 0):
        return 1
    else:
        return -1

def percep (weights , point):
    # First we take dot product of weights and points
    #note numpy objects treat * as element wise *
    inter = sum(weights*point)
    cls = classifier(inter)
    
    return cls

def AndDataGen(ports):
    #depending on number of ports generate training dataset. 
    #xdata holds all the bit combos in one column and all the 
    #bits of that patter of rows 
    #ex : xdata[0] = np.array([0,0,0]) like this
    xdata = np.zeros(((2**ports),ports),dtype = int)
    
    for i in range((2**ports)):
        #using format(X, 'type') returns the binary string 
        # format(5,'#07b') = 0b00101 , Note string length is 7 
        form = '#0{}b'.format(ports+2)
        string = format(i,form)
        for index in range(ports):
            xdata[i][index] = int(string[2+index])
            
    #now we return a hyper matrix whose highest selection index is
    # 0 for data and 1 for class then we have the second index for
    # particular bit combo
    return xdata

def AndClass (xdata,ports):
     xcls = np.zeros(((ports**2),1),dtype = int)
     for i in range(ports**2):
         xcls[i] = 2*(np.prod(xdata[i]))-1
     
     return xcls
     
def trainer (xdata,xcls,ports):
    w_old = np.zeros(((ports+1)),dtype = float)
    w_aft = np.ones(((ports+1)),dtype = float) 
    it = 1
    while((sum(abs(w_aft-w_old)).all()>0.1)):
        #now iterate through all points
        print('-'*50)
        print('iteration {}'.format(it))
        print('-'*50)
        for index in range(len(xcls)):
            #store previous aft in now old
            print('-'*50)
            print('index {}'.format(index))
            print('-'*50)
            w_old = w_aft
            print('w_old')
            print(w_old)
            
            points = xdata[index]
            points = np.append(points,[1],axis = 0)
            print('points')
            print(points)
            pred_cls = percep(w_old,points)
            if (pred_cls != xcls[index]):
                correction = xcls[index]*points
                print('correction')
                print(correction)    
                w_aft = w_old + correction
            else:
                w_aft = w_old
            print('w_updated')
            print(w_aft)  
            if(ports == 2):
                plotter(xdata,xcls,w_aft)        
        it +=1
        print('_'*50)
    return w_aft           
                    

def main():    
    ports = 2
    xdata = AndDataGen(ports)
    xcls = AndClass(xdata,ports)
    w = trainer(xdata,xcls,ports)
    print('final W : {}'.format(w)) 
    return

if __name__ == "__main__":
    main()