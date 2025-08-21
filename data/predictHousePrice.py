import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create a fictional dataset
data = {
    'area': [1500, 1800, 2400, 3000, 3500, 4000, 5000],
    'rooms': [3, 3, 4, 4, 5, 5, 6],
    'price': [400000, 450000, 600000, 650000, 700000, 800000, 850000]
}

df = pd.DataFrame(data)

# Features and target variable
X = df[['area', 'rooms']]  # Features
y = df['price']  # Target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict prices
y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE) for model evaluation
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Example of using the model for new predictions
new_house = np.array([[2500, 4]])  # Area = 2500, Rooms = 4
predicted_price = model.predict(new_house)
print(f'The predicted price for the new house is: ${predicted_price[0]:,.2f}')
