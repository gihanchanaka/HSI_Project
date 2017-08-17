#Import Library
import sklearn
import scipy
from sklearn import svm, datasets
import numpy as np
import matplotlib.pyplot as plt

# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2] # we only take the first two features. We could avoid this ugly slicing by using a two-dim dataset
y = iris.target
X = scipy.io.loadmat("Row_5628.mat")['B']
np.delete(X, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], axis=1)

y = np.array([int(i>250) for i in range(len(X))])
plt.figure()
for i in range(len(X)):
    if y[i]:
        color = 'r'
    else:
        color = 'b'
    plt.plot(X[i],color)

# Create SVM classification object
model = svm.SVC(kernel='rbf', C=1).fit(X, y)
model.score(X, y)

f2 = plt.figure()
test =scipy.io.loadmat("Row_5629.mat")['B']
np.delete(test, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], axis=1)
Z = model.predict(test)
print(Z)
for i in range(len(test)):
    if Z[i]:
        color = 'r'
    else:
        color = 'b'
    plt.plot(test[i], color)

"""
# Create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
np.arange(y_min, y_max, h))

Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
"""
plt.show()
