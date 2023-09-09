import numpy as np
import matplotlib.pyplot as plt
# Question 1:
arr1=np.random.randint(1,10,(3,3))
print("The Orginal Matrix:",arr1)
arr1trans= arr1.transpose()
print("The Transpose Matrix: ",arr1trans)
arr1det=np.linalg.det(arr1)
print("The Determent of Matrix: ",arr1det)
if arr1det!=0:
    arr1inv=np.linalg.inv(arr1)
    print("The Inverse of Matrix: ",arr1inv)




