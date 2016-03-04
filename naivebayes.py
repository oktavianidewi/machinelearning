from sklearn.naive_bayes import GaussianNB
import numpy as np

# assigning predictors and target variables
# ada 12 data
x = np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
y = np.array([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
z = np.array([3, 3, 3, 3, 4, 3, 3, 3, 4, 3, 4, 4, 4])

# create a Gaussian Classifier
model = GaussianNB()

# train the model using the training sets
model.fit(x, y)
model.fit(x, z)

# predict output
predicted = model.predict([ [1,2], [3,4] ])
print(predicted)