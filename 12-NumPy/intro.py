#numpy array is a list pro max
#Numpy = numeric python
#ndarray= n-dimensional array
import numpy as np
np1=np.array([1,0,2,3,4,5,6,7,8,9])
print(np1)

#shape
print(np1.shape)#its like a length of the array

#range
np2=np.arange(10)
print(np2)
 
#step
np3=np.arange(0,10,2)
print(np3)

#zeros
np4=np.zeros(10)
print(np4)

#multidimensional zeros
np5=np.zeros((2,10))
print(np5)

#full
np6=np.full((10),6)
print(np6)

#multidimensional full
np7=np.full((2,10),6)
print(np7)

#convert python lists to np
my_list=[1,2,3,4,5]
np8=np.array(my_list)
print(np8)