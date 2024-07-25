import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing

# Load the California housing dataset
housing = fetch_california_housing()
housing_df = pd.DataFrame(housing.data,columns=housing.feature_names)
housing_df['MedHouseVal'] = housing.target

# Display Basic Info on Data Set
print(housing_df.info())
print(housing_df.describe())

# Clean Data of Missing Values
housing_df.isnull().sum()

# Split the Data into Training and Test sets
x = housing_df.drop('MedHouseVal', axis=1)
y = housing_df['MedHouseVal']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Standardize the Data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Make Predictions
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Make Predictions 
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

# Calculate performance metrics
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f'Training MSE: {train_mse},Training R2: {train_r2}')
print(f'Testing MSE: {test_mse}, Testing R2: {test_r2}')

plt.figure(figsize=(10,7))
plt.scatter(y_test,y_test_pred,alpha=0.3)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted House Prices')
plt.show()