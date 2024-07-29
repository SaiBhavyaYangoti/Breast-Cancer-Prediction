# -*- coding: utf-8 -*-
"""breast cancer detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y8sNNYeurQt4_mC-E_Spsj8J7_JI4Oia

Importing libraries
"""

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.datasets
from sklearn.model_selection import train_test_split

"""Loading dataset"""

#loading dataset
data_frame=sklearn.datasets.load_breast_cancer()

#initially the data is in the form of a dictionary
print(data_frame)

"""Data preprocessing"""

#converting dictionary into pandas dataframe. here feature_names are the column names
df=pd.DataFrame(data_frame.data, columns=data_frame.feature_names)

df.head()

#naming the target column as target
df['target']=data_frame.target

#1 means malignant i.e. high chances of having cancer and 0 means beningn i.e. no cancer
df['target'].tail()

"""Separating features and target"""

x=df.drop(columns='target', axis=1)     #considering all the columns except target column as features
y=df['target']                          #considering target column as target

"""Splitting training and testing data"""

#20% of the data is splitted for testing and 80% for training
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=2)

#printing shapes of training and testing data
print(x.shape, X_train.shape, X_test.shape)

"""**Prediction models**

Logistic Regression
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create and train the model
logistic_regression_model = LogisticRegression()
logistic_regression_model.fit(X_train, y_train)

# Make predictions
y_pred_lr = logistic_regression_model.predict(X_test)

# Evaluate the model
accuracy_lr = accuracy_score(y_test, y_pred_lr)
print("Logistic Regression Accuracy:", accuracy_lr)

"""Multiple linear regression"""

import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

# Convert DataFrames to NumPy arrays
X_train_array = X_train.to_numpy()
X_test_array = X_test.to_numpy()

# Flatten the sequences for linear regression
X_train_flatten = X_train_array.reshape(X_train_array.shape[0], -1)
X_test_flatten = X_test_array.reshape(X_test_array.shape[0], -1)

# Create and train the model
linear_regression_model = LinearRegression()
linear_regression_model.fit(X_train_flatten, y_train)

# Make predictions (round to 0 or 1)
y_pred_linear = np.round(linear_regression_model.predict(X_test_flatten))

# Convert to binary predictions
y_pred_linear[y_pred_linear < 0] = 0
y_pred_linear[y_pred_linear > 1] = 1

# Evaluate the model
accuracy_linear = accuracy_score(y_test, y_pred_linear)
print("Multiple Linear Regression Accuracy:", accuracy_linear)

"""kNN classifier"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Convert DataFrames to NumPy arrays
X_train_array = X_train.to_numpy()
X_test_array = X_test.to_numpy()

# Flatten the sequences
X_train_flatten = X_train_array.reshape(X_train_array.shape[0], -1)
X_test_flatten = X_test_array.reshape(X_test_array.shape[0], -1)

# Create and train the model
knn_model = KNeighborsClassifier()
knn_model.fit(X_train_flatten, y_train)

# Make predictions
y_pred_knn = knn_model.predict(X_test_flatten)

# Evaluate the model
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print("KNN Accuracy:", accuracy_knn)

"""Random Forest Classifier"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Create and train the model
rf_model = RandomForestClassifier()
rf_model.fit(X_train_flatten, y_train)

# Make predictions
y_pred_rf = rf_model.predict(X_test_flatten)

# Evaluate the model
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print("Random Forest Accuracy:", accuracy_rf)

"""SVM (Support Vector Machine)"""

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Create and train the model
svm_model = SVC()
svm_model.fit(X_train_flatten, y_train)

# Make predictions
y_pred_svm = svm_model.predict(X_test_flatten)

# Evaluate the model
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print("SVM Accuracy:", accuracy_svm)

"""Gradient Boosting"""

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# Create and train the model
gb_model = GradientBoostingClassifier()
gb_model.fit(X_train_flatten, y_train)

# Make predictions
y_pred_gb = gb_model.predict(X_test_flatten)

# Evaluate the model
accuracy_gb = accuracy_score(y_test, y_pred_gb)
print("Gradient Boosting Accuracy:", accuracy_gb)

"""Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Create and train the model
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train_flatten, y_train)

# Make predictions
y_pred_dt = dt_model.predict(X_test_flatten)

# Evaluate the model
accuracy_dt = accuracy_score(y_test, y_pred_dt)
print("Decision Tree Accuracy:", accuracy_dt)

"""Neural Networks"""

from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras

#standardize the data
scaler=StandardScaler()
X_train_std=scaler.fit_transform(X_train)
X_test_std=scaler.transform(X_test)

#to get same accuracy score everytime we run
tf.random.set_seed(3)

#setting up the layers for neural network model
model = keras.Sequential([
                          keras.layers.Flatten(input_shape=(30,)),    #input layer (we are giving 30 neurons, since we have 30 features)
                          keras.layers.Dense(20, activation='relu'),   #hidden layers (20 neurons in hidden layer, as per our wish)
                          keras.layers.Dense(2, activation='sigmoid')   #output layer (2 neurons in output layer. This should always equal to the no.of categories in our target. Here 2 cat: B,M)
])

#compiling the NN
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#traning the model
history = model.fit(X_train_std, y_train, validation_split=0.1, epochs=10)

#checking loss and accuracy of test data
loss,accuracy=model.evaluate(X_test_std, y_test)
print("Neural networks accuracy: ", accuracy)

"""**Comparison plot**"""

import matplotlib.pyplot as plt

# List of algorithms and their accuracies
algorithms = ['Logistic Regression', 'Multiple Linear Regression', 'KNN', 'Random Forest', 'SVM', 'Gradient Boosting', 'Decision Tree','Neural Networks']
accuracies = [accuracy_lr, accuracy_linear, accuracy_knn, accuracy_rf, accuracy_svm, accuracy_gb, accuracy_dt, accuracy]

# Plot the bar graph
plt.figure(figsize=(10, 8))
bars = plt.bar(algorithms, accuracies, color='skyblue')
plt.xlabel('Algorithms')
plt.ylabel('Accuracy')
plt.title('Accuracy Comparison of Breast Cancer Prediction Algorithms')
plt.xticks(rotation=45, ha='right')
plt.ylim(0, 1)

# Add labels with percentages inside each bar
for bar, accuracy in zip(bars, accuracies):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{accuracy:.2%}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

"""As a result, Multiple Linear Regression performs well with an accuracy of 97.37%, followed by Random forest, Decision Tree and Neural Networks with an accuracy of 93.86%.

**Testing the model**
"""

#using neural networks model to predict breast cancer
input=(13.07,11.76,66.72,274.9,0.07684,0.05513,0.06734,0.01211,0.1432,0.05787,0.4062,1.18,2.635,28.47,0.006534,0.008796,0.07835,0.007445,0.02406,0.001769,12.98,25.72,82.98,516.5,0.1132,0.09721,0.04777,0.03517,0.2543,0.06423)

#change the input into a numpy array
arr=np.asarray(input)

#reshaping the numpy array
arr2=arr.reshape(1,-1)

#standardizing the input data
input_std=scaler.transform(arr2)

prediction=model.predict(input_std)
print(prediction)

prediction_label=[np.argmax(prediction)]
print(prediction_label)

if(prediction_label[0]==0):
  print('The tumor is Benign')

else:
  print('The tumor is Malignant')
