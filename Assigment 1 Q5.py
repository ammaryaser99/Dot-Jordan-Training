from Assigment_1_Q1 import *
def ListToMatrix(list):
    for row in list:
        print(row)
        rez = [[list[j][i] for j in range(len(list))] for i in range(len(list[0]))]
    arr=np.array(rez)
    print(arr)
test=[[1,2,3,4,5],[2,3,4,5,6],[6,7,2,1,4]]
ListToMatrix(test)