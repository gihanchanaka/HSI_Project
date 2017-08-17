import scipy.io
import numpy as np
import curvefit
import matplotlib.pyplot as plt
import scipy.misc as smp
import derrivative

m=[]
wavelengths = []
def loadfiles(start, end):
    for i in range(start, end + 1):
        filename = "Row_"
        filename += str(i) + ".mat"
        mat = scipy.io.loadmat(filename)['B']
        mat = np.delete(mat, [i for i in range(53)], axis=1) #-----------------------------------------------------------------63

        m.append(mat)
    fh = open("wavelengths.txt")
    while 1:
        try:
            wavelengths.append(float(fh.readline()))
        except:
            break

print("Started loading files...")
loadfiles(5628, 5633)
print("loaded")


def norm(v):
    n = 0
    for i in range(len(v)):
        n += v[i] ** 2
    return n ** 0.5

data = [[[0 for _ in range(len(m[0][0]))] for _ in range(len(m[0]))] for _ in range(len(m))]
ddatadl = [[[0 for _ in range(len(m[0][0]))] for _ in range(len(m[0]))] for _ in range(len(m))]

print("Started normalizing data")
for y in range(len(m)):
    for x in range(len(m[0])):
        n = norm(m[y][x])
        for z in range(len(m[0][0])):
            temp = float(m[y][x][z])
            data[y][x][z] = temp/max(0.000000000001, n)
            if z != 0:
                ddatadl[y][x][z-1] = (data[y][x][z] - data[y][x][z-1]) / (wavelengths[z] - wavelengths[z-1])

        nn = norm(data[y][x])
print("normalized")

fig = plt.figure()
plt.plot(wavelengths, ddatadl[0][100])
plt.figure()
plt.plot(wavelengths, data[0][100])
plt.show()
def adjustingData(M):
    mean=[0 for _ in range(len(M[0][0]))]
    for z in range(len(M[0][0])):
        sum=0
        for y in range(len(M)):
            for x in range(len(M[0])):
                sum+=M[y][x][z]
        mean[z]=sum/(len(M)*len(m[0]))

    for y in range(len(M)):
        for x in range(len(M[0])):
            for z in range(len(M[0][0])):
                M[y][x][z] = np.exp(M[y][x][z]-mean[z])

adjustingData(data)


def project(v):
    projection = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
    for y in range(len(data)):
        for x in range(len(data[0])):

            for z in range(len(data[0][0])):
                projection[y][x] += np.exp(data[y][x][z]-v[z])**2

    return projection
print("started projecting")
pr = project(curvefit.gy)
print('projection complete')


def live_plot(arr):
    n, m = arr.shape

    g = []
    for x in arr:
        x_ = np.mean(x)
        xs = np.std(x)
        y = (x - x_) / xs
        ymin = min(y)
        ymax = max(y)
        z = ((y - ymin) / (ymax - ymin))
        g.append(z)

    pixelz = [[[0,0,0] for _ in range(m)] for _ in range(n)]

    for i in range(n):
        print("plotting dataset {}".format(i))
        for j in range(m):
            pixelz[i][j] = [int(255*g[i][j]),int(255*g[i][j]),int(255*g[i][j])]

    img = smp.toimage(pixelz)  # Create a PIL image
    img.show()




print("started plotting")
live_plot(np.array(pr))
live_plot(derrivative.findSpikes(m,wavelengths,"Sajani akka dena eka"))
plt.show()
print("plotting complete")



