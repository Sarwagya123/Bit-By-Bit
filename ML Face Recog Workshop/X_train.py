import numpy as np

a = np.load('D:\ML Workshop\Raghav.npy')
b = np.load('D:\ML Workshop\sarwagya.npy')

c=np.insert(b,45,a,axis=0)
print(np.shape(c))

np.save('X_train_new',c)