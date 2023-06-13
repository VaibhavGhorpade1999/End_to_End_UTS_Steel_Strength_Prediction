# Ultimate Tensile Strength (UTS) Prediction of Austenitic Steel using Machine Learning

## Introduction

- This project aims to predict the Ultimate Tensile Strength (UTS) of Austenitic Steel using machine learning techniques. 
- The goal is to reduce cost and time in predicting mechanical properties, benefiting manufacturers and designers in the field of advanced material science and engineering.

## Objective

1. Improve UTS prediction accuracy to minimize material testing costs and optimize product performance.
2. Enhance decision-making by providing reliable UTS estimates during the design and manufacturing process.

## Data Understanding

- The dataset used in this project is sourced from [www.phase-trans.msm.cam.ac.uk.](http://www.phase-trans.msm.cam.ac.uk/) 
- It contains 31 features and 2180 instances, including chemical composition, sectional size, temperature, and process parameters of the Austenitic Steel. 
- The target feature is the Ultimate Tensile Strength (UTS).
  <img width="619" alt="image" src="https://github.com/VaibhavGhorpade1999/End_to_End_UTS_Steel_Strength_Prediction/assets/115491376/729d7824-880d-4e65-8fb9-06647624d390">


## Data Preparation

- Data cleaning and preparation steps were performed to ensure the quality of the dataset. 
- Missing data was handled, and columns with high missing values or insignificant contribution to UTS prediction were dropped. 
- Categorical features were encoded manually to numeric values.

## Modeling

Several regression models were built to predict the UTS of Austenitic Steel. The models used include:
1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. K-Neighbors Regressor
5. Support Vector Regressor
6. Bagging Regressor with Decision Tree Regressor
7. AdaBoost Regressor
8. Gradient Boosting Regressor
9. XGBoost Regressor
10. Ridge Regression
11. Lasso Regression

## Evaluation and Tuning
![image](https://github.com/VaibhavGhorpade1999/End_to_End_UTS_Steel_Strength_Prediction/assets/115491376/2d376e3c-d5d0-4e8f-8f79-c08d4d1cf027)


- The models were evaluated using K-Fold Cross Validation and performance metrics such as R-squared score. 
- Hyperparameter tuning was performed using GridSearchCV to optimize the models' performance.

## Deployement on AWS

![Ultimate Tensile Strength Prediction - Google Chrome 2023-06-13 18-55-04](https://github.com/VaibhavGhorpade1999/End_to_End_UTS_Steel_Strength_Prediction/assets/115491376/a7f1cab8-d582-42ef-b4db-3496740e28d4)


## Best Model - Justification and Conclusion

- The XGBoost Regressor, without hyperparameter tuning and after removing 13 outliers, achieved the best performance with an accuracy of 95.15%. 
- This model provides reliable predictions for the Ultimate Tensile Strength of Austenitic Steel.

## Conclusion

- This project demonstrates the successful application of machine learning techniques in predicting the UTS of Austenitic Steel. 
- The developed model can assist manufacturers and designers in material science and engineering to optimize product performance, reduce costs, and make informed decisions during the design and manufacturing process.

## Challenges Faced

- During the project, some challenges were encountered, including dealing with missing data, ensuring data quality, and tuning hyperparameters. 
- These challenges were addressed through data cleanup, feature selection, and hyperparameter tuning techniques.

## Business Insights

- The implementation of machine learning techniques in predicting the UTS of Austenitic Steel provides valuable business insights. 
- It highlights the potential of data science and analytics in the field of material sciences, offering increased accuracy and reliability in predicting mechanical properties. 
- The project's approach contributes to cost and time reduction, improved UTS prediction, and enhanced decision-making.


