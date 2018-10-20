import csv
from sklearn import svm, metrics
from numpy import genfromtxt
import numpy as np

dataset = genfromtxt('train.csv', delimiter=",")[1:]
labels = [x[0] for x in dataset]
data = [x[1:] for x in dataset]

n_samples = len(labels)
n_features = len(data[0])

print("Number of samples: " + str(n_samples) + ", number of features: "+ str(n_features))

# a support vector classifier
classifier = svm.LinearSVC()

split_point = int(n_samples * 0.66)

# using two thirds for training
# ans one third for testing

labels_learn = labels[:split_point]
data_learn = data[:split_point]

labels_test = labels[split_point:]
data_test = data[split_point:]

print("Training: " + str(len(labels_learn)) + " Test: " + str(len(labels_test)))

# Learning Phase
classifier.fit(data_learn, labels_learn)

# Predict Test Set
predicted = classifier.predict(data_test)

# classification report
print("Classification report for classifier %s:n%sn" % (classifier, metrics.classification_report(labels_test, predicted)))

# confusion matrix
print("Confusion matrix:n%s" % metrics.confusion_matrix(labels_test, predicted))
