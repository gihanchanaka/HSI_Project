import scipy.io
import matplotlib.pyplot as plt
import numpy as np

x_temp = scipy.io.loadmat('rutile_wavelength.mat')['OriginWhitePlains']
fx_temp = scipy.io.loadmat('rutile_reflectance.mat')['AlexanderCounty']
x = [0 for _ in range(len(x_temp))]
fx = [0 for _ in range(len(fx_temp))]
for i in range(len(x)):
    x[i] = float(x_temp[i][0][0])*1000

x.reverse()
for i in range(len(fx)):
    fx[i] = float(fx_temp[i])
plt.figure()
plt.plot(x,fx)
gy= []
y=[]

inputs = open('WaveBansInPixelData.txt', 'r')
def readinput():
    print("fd")
    x_input = float(inputs.readline().strip())
    print(x_input)
    y.append(x_input)

    if x_input < 2080 or x_input > 25000:

        return -1
    i = 0
    while x[i] < x_input:
        i += 1

        if i == len(x):
            print("NO X VALUE FOUND")
            return -1
    return (fx[i] + fx[i+1])/2

while 1:
    try:

        temp = readinput()
        gy.append(temp)
    except:
        break
plt.figure()
plt.plot(y,gy)
plt.show()