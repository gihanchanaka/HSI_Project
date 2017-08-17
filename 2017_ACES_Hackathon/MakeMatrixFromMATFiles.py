from __future__ import division
import scipy.io
import numpy as np

m = []
def f(filename):
    mat = scipy.io.loadmat(filename)['B']
    np.delete(mat, [i for i in range(10)], axis=1)
    m.append(mat)

def g(start, end):
    for i in range(start, end+1):
        filename = "data/Row_"
        filename += str(i)
        f(filename)

g(5627,5803)

def norm(v):
    n=0
    for i in range(len(v)):
        n+=v[i]**2
    return n**0.5

for y in range(len(m)):
    for x in range(len(m[0])):
        n = norm(m[y][x])
        for z in range(len(m[0][0])):

            m[y][x][z] = 1.0*m[y][x][z]/n

        nn = norm(m[y][x])
        print(n,nn)

