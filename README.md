# Task 4: Movie Rating Prediction

# Arch Technologies Data Science Internship

## 1. Project Overview
   
The goal of this project is to build a machine learning model that predicts a user's rating for a specific movie. By analyzing historical data of movie attributes and user demographics, the model can estimate how a user might perceive a film they haven't watched yet—a fundamental component of modern recommendation engines.

## 2. Dataset Description

The analysis utilizes the synthetic_movie_ratings.csv dataset, which includes 7,500 entries. Key features used for prediction include:

•	Movie Attributes: Genre, Release Year, Duration (Minutes), Budget (Million USD), and Director Popularity Score.

•	User Demographics: Age, Gender, Country, and Subscription Type.

•	Target Variable: Rating (on a scale of 1.0 to 5.0).

## 3. Methodology

## 3.1 Data Preprocessing

•	Feature Selection: Features were selected based on their relevance to a movie's appeal and a user's likely preference.

•	Categorical Encoding: Since machine learning models require numerical input, LabelEncoder was used to transform categorical text (Genre, Gender, Country, Subscription Type) into numerical formats.

•	Data Splitting: The dataset was partitioned into a Training Set (80%) to train the model and a Testing Set (20%) to evaluate its accuracy on unseen data.

## 3.2 Model Selection

I implemented a Random Forest Regressor. This ensemble learning method was chosen for its ability to:

1.	Handle both numerical and categorical data effectively.
  
2.	Capture non-linear relationships (e.g., how specific age groups prefer specific genres).
  
3.	Provide "Feature Importance" scores to show which factors drive movie ratings.
  
## 4. Performance Results
   
The model was evaluated using standard regression metrics:

•	Mean Absolute Error (MAE): 0.48 On average, the predicted rating is within 0.48 stars of the actual rating.

•	Root Mean Squared Error (RMSE): 0.59

•	R-squared Score (R²): 0.19

## 4.1 Feature Importance (Top Drivers)

The model identified the following as the most significant predictors of a movie rating:

1.	Budget (38.9%): Higher production value is the strongest indicator of rating consistency in this dataset.
  
2.	Director Popularity (13.5%): The reputation of the director significantly influences user scores.
  
3.	Duration (11.9%): Movie length is a notable factor in how users rate their experience.
  
## 5. Conclusion
The Random Forest model successfully predicts user ratings with high precision `(MAE < 0.5)`. These insights allow Arch Technologies to prioritize content based on director popularity and production scale to maximize user satisfaction.
________________________________________
Submitted by: Nikoro Omosefe Benita

Date: March 27, 2026

