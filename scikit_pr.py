import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model with incorrect parameters
incorrect_model = LinearRegression(fit_intercept=False)
incorrect_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = incorrect_model.predict(X_test)

# Evaluate the model with mean absolute error (incorrect metric)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error (Incorrect Metric): {mae}')

# Plot the incorrect regression line
plt.scatter(X_test, y_test, color='black', label='Actual Data')
plt.plot(X_test, y_pred, color='red', linewidth=3, label='Incorrect Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Incorrect Linear Regression Prediction')
plt.legend()
plt.show()
