# import from library
from sklearn import svm
import numpy as np

# x as predictor and y as target for training dataset and xtest (predictor) of testdataset
x = np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
y = np.array([1, 2, 1, 2, 1, 3, 3, 3, 3, 4, 3, 3])
# z = svm.array([3, 3, 3, 3, 4, 3, 3, 3, 4, 3, 4, 4, 4])
xtest = [ [1,2], [3,4] ]

# create svm classification object
# model = svm.svc(kernel = 'linear', c=1, gamma=1)
model = svm.SVC(kernel = 'linear', gamma=1)
model.fit(x, y)
model.score(x, y)

predicted = model.predict(xtest)
print(predicted)

# tes
# aku coba
# okee
