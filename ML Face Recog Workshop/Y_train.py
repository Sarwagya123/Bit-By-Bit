import numpy as np 
a=np.zeros((45,1))
b=np.ones((45,1))
c=np.insert(a,45,b,axis=0)
print(c)
np.save("Y_train",c)