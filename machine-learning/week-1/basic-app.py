import numpy as np
import pandas as pd
import pickle
from fastapi import FastAPI
import uvicorn
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from pydantic import BaseModel

import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('The_name_of_the_dataset', path='the_path_you_want_to_download_the_files_to', unzip=True)

# Creating FastAPI instance
app = FastAPI()

# Creating class to define the request body
# and the type hints of each attribute
class request_body(BaseModel):
	old_balanceOrg,
	amount,
	new_balanceOrig,
	TRANSFER : bool
	newbalanceDest,
	step : int
	oldbalanceDest,
	PAYMENT: bool
	CASH_OUT: bool
	DEBIT: bool
	CASH_IN: bool
	C: bool

# Loading Iris Dataset
#iris = load_iris()

# # Getting our Features and Targets
# X = iris.data
# Y = iris.target

# # Creating and Fitting our Model
# clf = GaussianNB()
# clf.fit(X,Y)
# Modelling
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

# Tree Visualisation
from sklearn.tree import export_graphviz
from IPython.display import Image
import graphviz
# Split the data into features (X) and target (y)
X = df.drop('isFraud', axis=1)
y = df['isFraud']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Creating an Endpoint to receive the data
# to make prediction on.
@app.post('/predict')
def predict(data : request_body):
	# Making the data in a form suitable for prediction
	test_data = [[
			data.old_balanceOrg,
	        data.amount,
	        data.new_balanceOrig,
	        data.TRANSFER,
	        data.newbalanceDest,
	        data.step,
	        data.oldbalanceDest,
	        data.PAYMENT,
	        data.CASH_OUT,
	        data.DEBIT,
	        data.CASH_IN,
	        data.C
	]]
	
	# Predicting the Class
	class_idx = rf.predict(test_data)[0]
	
	# Return the Result
	return { 'class' : df.target_names[class_idx]}
