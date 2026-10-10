# Sales Analysis, EDA, and Regression Model Python Script

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load dataset (Global Superstore Orders sheet or sample data)
# df_orders = pd.read_excel('Sales_Performance_Dashboard.xlsx', sheet_name='Orders')

# 2. Exploratory Data Analysis (EDA) Summary
print("--- Exploratory Data Analysis ---")
# category_summary = df_orders.groupby('Category').agg(
#     Total_Sales=('Sales', 'sum'),
#     Average_Sales=('Sales', 'mean'),
#     Total_Profit=('Profit', 'sum'),
#     Total_Quantity=('Quantity', 'sum')
# ).reset_index()
# print(category_summary)

# 3. Regression Model for Sales Prediction
# X = df_orders[['Quantity', 'Discount', 'Profit', 'Shipping Cost']]
# y = df_orders['Sales']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(f"R2 Score: {r2_score(y_test, y_pred):.4f}")
# print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
