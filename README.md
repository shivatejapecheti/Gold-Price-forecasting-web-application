# Gold-Price-forecasting-web-application

 <div align="justify"> The Gold Price Prediction Web App is a Django-based application that leverages machine learning techniques to predict gold prices. This detailed overview provides insights into the methodologies, features, technologies used, and the functionality of the application. </div>

 ## Methodology

1. Data Collection with Yahoo Finance
   The application fetches historical gold price data from Yahoo Finance using the yfinance library. This data includes the daily closing prices of the Gold ETF ('GLD').

2. Exploratory Data Analysis (EDA

Features:
+ Closing Price Plot: Visualizes the historical closing prices of the Gold ETF using Plotly.
+ Linear Regression Model: Utilizes a linear regression model with 3-day and 9-day moving averages as explanatory variables.
+ Prediction Plot: Compares predicted gold prices with actual prices for the test dataset.
+ Cumulative Returns: Calculates and displays cumulative returns based on predicted price movements.

3. Model Training and Testing
   The dataset is split into training and testing sets, with 80% used for training the linear regression model and 20% for testing.

4. Gold Price Prediction
   The trained linear regression model is used to predict gold prices for the test dataset, and the results are compared with actual prices.

5. Web Application Features
   
Pages:
+ Home Page: Provides an overview of closing price plots, prediction plots, cumulative returns, and current predictions.

+ Information Page: Details about the linear regression model, R-squared score, and other relevant information.

+ Plots Page: Displays closing price, prediction, and cumulative returns plots.

+ Gold Price Page: Fetches and displays real-time gold prices from an external API.

Additional Pages:

Cookie Page: Demonstrates setting and retrieving cookies.

Timezone Page: Demonstrates setting and retrieving user timezones.

Info Page: Displays gold price information over the past 15 days and full historical data.


![Overview](https://github.com/shivatejapecheti/Gold-Price-forecasting-web-application/assets/126412107/62567332-eaba-4c7d-afc1-1f31bcc10773)
