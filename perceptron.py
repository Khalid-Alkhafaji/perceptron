import os
import sys
import numpy as num


train_data = []
weights = []
def Readfile():
 
    with open("training-data.txt") as file:
        cnt,ind = 0,0
        train = num.zeros(64, dtype=int)
        for line in file:
            if cnt == 0:
                train[0] = 1
                ind+=1
                cnt+=1
                for element in line:
                    if element=='#':
                        train[ind] = 1
                        ind+=1
                    elif element=='*':
                        train[ind] = -1
                        ind+=1
                    
            elif cnt==9:
                cnt,ind = 0,0
                train_data.append(train)
                train = num.zeros(64,dtype=int)
            else:
                for element in line:
                    if element=='#':
                        train[ind] = 1
                        ind+=1
                    elif element=='*':
                        train[ind] = -1
                        ind+=1
                cnt+=1
        return train_data
 


def Actfunc (y_in):
    
    if y_in > 0:
        y_out = 1
    else:
        y_out = -1
    return y_out



def Learn(train_data):
    weights = []
    for j in range(0, 7):
        weight = num.random.rand(1, 64)
        epochs = 1
        while True:
            old_weights = weights.copy()
            for i in range(0, len(train_data)):
                x = train_data[i]
                y_in = weight.dot(x)
                y = Actfunc(y_in)
                if i % 7 == j:
                    t = 1
                else:
                    t=-1	    
                if y != t:
                    weight += t * x.T			

            if num.array_equal(old_weights, weights):
                break
            
            epochs += 1
        weights.append(weight)
    print (weights)
    return weights
"""    epoch = 0
    for j in range(0,7):
        weight = num.random.rand( 64,)
        backstep = weight.copy()
        for i in range (0, len(train_data)):
            while True:
                s = train_data[i]
                y_in = weight.dot(s)
                Actfunc(y_in)
                if i%7 == j:
                    target = 1
                else :
                    traget = -1
                if Actfunc(y_in) != target :                        
                    weight += target * train_data[i]
                if num.array_equal(backstep, weight):
                    weights.append(weight)
                    break 
            print(weights)
    print (weights)
    return weights"""



 

def test (weights):
    character = input("Please enter character: ")
    if character == "A":
        targ = 0
    elif character == "B":
        targ = 1
    elif character == "C":
        targ = 2
    elif character == "D":
        targ = 3
    elif character == "E":
        targ = 4
    elif character == "J":
        targ = 5
    elif character == "K":
        targ = 6
    with open("test-data.txt") as file:
        test = num.zeros(64, dtype=int)
        ind = 1
        test[0]== 1
        for line in file:
            for element in line:
                if element=='#':
                    test[ind] = 1
                    ind+=1
                elif element=='*':
                    test[ind] = -1
                    ind+=1
        testweight = num.zeros((64,1), dtype=int)
        for j in range (0, 7):
            testweight = weights[j]
            y_in = testweight.dot(test)
            if Actfunc (y_in) == 1 and j == targ:
                print("Perceptron recognized character")
            elif Actfunc (y_in) == 1 and j != targ:
                print (j)
                print("Perceptron failed")
            elif Actfunc (y_in) == -1 and j == targ:
                print("Silly perceptron")
            #print (weight)
                

           
def main():
     Learn(Readfile())
     test(Learn(Readfile()))
     




