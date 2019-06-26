# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:17:18 2019

@author: Lakshay
"""

import pandas as pd

data=pd.read_csv("train.csv")

features=data.iloc[:,1:].values
labels=data.iloc[:,0:1].values

from sklearn.cross_validation import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.25,random_state=0)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Fitting Kernel SVM to the Training set
# kernels: linear, poly and rbf
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
#score = classifier.score(features_test,labels_test)
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = features_train, y = labels_train, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())


#Visualization

x_min, x_max = features_train[:, 0].min() - 1, features_train[:, 0].max() + 1
y_min, y_max = features_train[:, 1].min() - 1, features_train[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))
# Obtain labels for each point in mesh using the model.
# ravel() is equivalent to flatten method.
# data dimension must match training data dimension, hence using ravel
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# Plot the points
plt.plot(features_test[labels_test == 0, 0], features_test[labels_test == 0, 1], 'ro', label='Class 1')
plt.plot(features_test[labels_test == 1, 0], features_test[labels_test == 1, 1], 'bo', label='Class 2')
#plot the decision boundary
plt.contourf(xx, yy, Z, alpha=1.0)

plt.show()