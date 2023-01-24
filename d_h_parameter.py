import numpy as np
import matplotlib.pyplot as plt

def dh(x):
    product = np.array([[1,0,0,0],
                       [0,1,0,0],
                       [0,0,1,0],
                       [0,0,0,1]])
    lin, col = np.shape(x)
    for i in x:
        aux = np.array([[np.cos(i[0]),  -np.sin(i[0])*np.cos(i[3]), np.sin(i[0])*np.sin(i[3]),  i[2]*np.cos(i[3])],
                        [np.sin(i[0]),  np.cos(i[0])*np.cos(i[3]),  -np.cos(i[0])*np.sin(i[3]), i[2]*np.sin(i[3])],
                        [0,             np.sin(i[3]),               np.cos(i[3]),               i[1]],
                        [0,             0,                          0,                          1]])
        product = np.dot(product,aux)

    return product

theta1 = np.linspace(0,np.pi,3)
theta2 = np.linspace(0,np.pi,3)
theta3 = np.linspace(0,np.pi,3)

test = np.array([[theta1, 0, 150, 0],
              [theta2, 0, 0, np.pi/2],
              [theta3, 100, 0, 0]])
#print(dh(test))

n = []

for a in theta1:
    for b in theta2:
        for c in theta3:
            test = np.array([[a, 0, 150, 0],
                             [b, 0, 0, np.pi/2],
                             [c, 100, 0, 0]])
            d = dh(test)#[:3,3:]
            n.append(d)
            #d = np.append(d,e)

            #np.append(n,e)
#print(n)
#print("\n\n\n\n")

for j in n:
    print (j)      
print(np.shape(n) )               
'''fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection="3d")'''
