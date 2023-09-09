from Assigment_1_Q1 import *
# Question 3:
def check (arr):
    counter=0
    max=0
    arr2=list(arr)
    for i in range(0,len(arr2)):
        if arr2[i]=="0":
            counter+=1
        else:
            if counter>max:
                max=counter
                counter=0
            else:
                counter=0
    return max
tt = "0000000000"
print("The Max Sequence of Zeros is: ",check(tt))