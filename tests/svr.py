'''
Created on 27-Apr-2014

@author: vr
'''
from sklearn.svm import SVR
import numpy as np
import pylab as pl

X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()
################################################
# Add noise to targets
y[::5] += 3 * (0.5 - np.random.rand(8))
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
print y
print y[5],y[1]
y_rbf = svr_rbf.fit(X, y).predict(X)
y_lin = svr_lin.fit(X, y).predict(X)
y_poly = svr_poly.fit(X, y).predict(X)
########################
pl.scatter(X, y, c='k', label='data')
pl.hold('on')
pl.plot(X, y_rbf, c='g', label='RBF model')
pl.plot(X, y_lin, c='r', label='Linear model')
pl.plot(X, y_poly, c='b', label='Polynomial model')
pl.xlabel('data')
pl.ylabel('target')
pl.title('Support Vector Regression')
pl.legend()
pl.show()