import scipy.io
import matplotlib.pyplot as plt

x_temp = scipy.io.loadmat('ilmenite_wavelengths.mat')
fx_temp = scipy.io.loadmat('ilmenite_reflectance.mat')
x_temp = x_temp['OriginIlmenMountains']
fx_temp = fx_temp['Urals']

x = [0 for _ in range(len(x_temp))]
fx = [0 for _ in range(len(fx_temp))]
for i in range(len(x)):
    x[i] = float(x_temp[i][0]) * 1000

x.reverse   ()
for i in range(len(fx)):
    fx[i] = float(fx_temp[i])
plt.figure()
plt.plot(x, fx)
gy = []
y = []

inputs = open('wavelengths.txt', 'r')

def readinput():

    x_input = float(inputs.readline().strip())

    y.append(x_input)

    if x_input < 2080 or x_input > 25000:
        return 0
    i = 0
    while x[i] < x_input:
        i += 1

        if i == len(x):
            print("NO X VALUE FOUND")
            return 0
    return (fx[i] + fx[i + 1]) / 2


while 1:
    try:
        temp = readinput()
        gy.append(temp)
    except:
        break
fh = open("ilmenite_sat.txt", "w")
for i in range(len(y)):
    fh.write("{} {}\n".format(y[i], gy[i]))
plt.figure()
plt.plot(y, gy)
