__author__ = 'Gihan'

import scipy.io
import matplotlib.pyplot as plt
import numpy as np

mat = scipy.io.loadmat('data/Row_5627.mat');
t = np.arange(0.0, len(mat[0]))
iplt.plot(t,mat[1])
plt.show()
