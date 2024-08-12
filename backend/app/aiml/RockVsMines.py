import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load and prepare data
def load_and_train_model():
    sonar_data = pd.read_csv('../resources/RockVsMines.csv', header=None)
    X = sonar_data.drop(columns=60, axis=1)
    Y = sonar_data[60]
    
    # Split the data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)
    
    # Train the Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    
    # Calculate accuracy (for reference)
    X_train_prediction = model.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
    print('Accuracy on training data:', training_data_accuracy)
    
    X_test_prediction = model.predict(X_test)
    test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
    print('Accuracy on test data:', test_data_accuracy)
    
    return model

# Predict function using the trained model
def predict_object(model, input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = model.predict(input_data_reshaped)
    
    if prediction[0] == 'R':
        return 'The object is a Rock'
    else:
        return 'The object is a Mine'
