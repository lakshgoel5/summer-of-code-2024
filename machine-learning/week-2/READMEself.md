# Approach
1. Started Encoding dates to extract months. Later understood that datetime formats exist in python to understand dates.
2. Started with Time series course on Kaggle
3. Did a course on data visualization to understand graph plotting in python
4. Analysed the data for NaN values (found NaN values in oil.csv only)
5. Summed up all sales using dates as index and assigned data to "average_sales" (Most sources used mean instead of sum, but mean dosen't seem to be correct representation of sales to me)
6. Analyzed average_sales for:
    * Time-step relations: Came out to be Linear\
    ![image](machine-learning\week-2\assets\timesteplineargraph.png)
    * Lag relation: Came to be Linear\
    ![image](machine-learning\week-2\assets\laglineargraph.png)
6. Trained model on Linear Regression for both time-step and lag features
7. Analyzed Seasonality for year 2017 only(On training model on all years using linear regression initially, but was not getting good results)
8. Trained model on Linear Regression (model_1) with fourier features and then deseasoned the data by subtracting y_pred from y
9. To get more accurate results, analyzed holidays.csv
10. Trained a Linear Regression model on dates of holidays and the sales. Added the prediction of this model to model_1 and got better results. \
![image](machine-learning\week-2\assets\seasonality_training_with_holodays.png)
11. Then made a hybrid model of
    * Linear Regression (X_1)
    * XGBRegressor (X_2)
12. X_1: Trained sum of sales on linear regression. Predictions of this model were subtracted from y to get y_residual
13. X_2: Trained On-promotion with y_residual and then combined both predictions
14. Tried Prophet but dosen't seem to be helpful sinces only one column can be given as input: sum of sales. Hybrid model seemed better.
# Challanges
1. First I was confused how to handle dates. There were 1684 dates, 56 mm//yyyy, 5 years.
    * So I initially converted mm//yyyy strings to onehot
    * later I came to know about np.datetime64 to handle dates
2. Sometimes I copied some commands from google to reshape my dataset, but those commands didn't go as expected, so had to do alloperations again.
3. Couldn't capture basic essence of trends, so left that part
4. After implementing hybrid model, few families like BABY CARE, BOOKS, AUTOMOBILE were not predicted well. Still couldn't figure out why this happened.
5. Tried ARIMA, but couldn't understand it. (want a hands-on session on it)
# Results
1. Time-step and Lag, both features were present in this training data
2. LinearRegression was working well since there was a (almost) linear graph of both time-step and lag features.
3. Including holidays in model turned out to fruitful
4. Families whose sales were in thousands were predicted well by hyvrid model.\ ![image](machine-learning\week-2\assets\Hybrid_model_results_1.jpg) \ ![image](machine-learning\week-2\assets\Hybrid_model_result_2.jpg)