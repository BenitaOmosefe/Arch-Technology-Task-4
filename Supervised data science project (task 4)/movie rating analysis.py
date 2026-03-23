import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# 1. Load the dataset
dataset = pd.read_csv('synthetic_movie_ratings.csv')

# 2. Preprocessing & Feature Selection
# We use characteristics of the movie and user to predict the rating
features = ['Genre', 'Release_Year', 'Duration_Minutes', 'Budget_Million_USD', 
            'Director_Popularity_Score', 'Age', 'Gender', 'Country', 'Subscription_Type']
X = dataset[features].copy()
y = dataset['Rating']

# Encode categorical text into numbers
le = LabelEncoder()
for col in ['Genre', 'Gender', 'Country', 'Subscription_Type']:
    X[col] = le.fit_transform(X[col].astype(str))

# 3. Split Data into Training (80%) and Testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 5. Evaluate the Model
y_pred = rf_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Task 4 Results:")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

# 6. Identifying Key Drivers
importances = pd.Series(rf_model.feature_importances_, index=features).sort_values(ascending=False)
print("\nTop 3 Rating Predictors:")
print(importances.head(3))