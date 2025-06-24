import pandas as pd

# Load the data
df = pd.read_csv('Churn.csv')

# Quick look at the data
print(df.head())
print(df.info())
print(df['Churn'].value_counts())  # Assuming 'Churn' is the target column

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Example: Encode categorical columns
for col in df.select_dtypes(include=['object']).columns: 
    if col != 'Churn':  
        df[col] = LabelEncoder().fit_transform(df[col])

# Encode target if needed
if df['Churn'].dtype == 'object':
    df['Churn'] = LabelEncoder().fit_transform(df['Churn'])

# Split features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

import tensorflow as tf
from tensorflow import keras

# Simple neural network
model = keras.Sequential([
    keras.layers.Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')  # Binary output
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy:.2f}')



from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))


