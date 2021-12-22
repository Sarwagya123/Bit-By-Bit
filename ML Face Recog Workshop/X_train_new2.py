import numpy as np

a = np.load('D:\ML Workshop\Raghav.npy')
b = np.load('D:\ML Workshop\sarwagya.npy')

c=np.insert(b,45,a,axis=0)
c=np.reshape(c,(90,30000))
print(np.shape(c))
np.save("X_Train_new2",c)
