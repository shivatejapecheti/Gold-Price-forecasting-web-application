# Gold-Price-forecasting-web-application

 <div align="justify"> The Gold Price Prediction Web App is a Django-based application that leverages machine learning techniques to predict gold prices. This detailed overview provides insights into the methodologies, features, technologies used, and the functionality of the application. </div>

 
![Overview](https://github.com/shivatejapecheti/Gold-Price-forecasting-web-application/assets/126412107/62567332-eaba-4c7d-afc1-1f31bcc10773)

Technologies Used: <div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" height="40" alt="django logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="40" alt="pandas logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="40" alt="html5 logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="40" alt="css3 logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="40" alt="javascript logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
</div>

###

1. Django (Web Framework): Provides a robust and scalable web application structure.
  
2. Pandas and NumPy (Data Analysis): Used for data manipulation and analysis.
  
3. Scikit-Learn (Machine Learning): Implements the linear regression model for gold price prediction.
  
4. YFinance (Yahoo Finance API): Fetches historical gold price data for analysis.
  
5. Plotly (Data Visualization): Creates interactive and visually appealing plots.
  
6. Pytz (Timezone Handling): Manages user timezones.
  
7. Requests (HTTP Library): Used for integrating external API for real-time gold prices.
  
8. HTML, CSS, JavaScript (Frontend): Standard web technologies for frontend development.

9. Gold API (External Gold Price API): An external API is integrated to fetch real-time gold prices.

 ## Methodology

1. Data Collection with Yahoo Finance
   The application fetches historical gold price data from Yahoo Finance using the yfinance library. This data includes the daily closing prices of the Gold ETF ('GLD').

2. Exploratory Data Analysis (EDA) 

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

+ Cookie Page: Demonstrates setting and retrieving cookies.

+ Timezone Page: Demonstrates setting and retrieving user timezones.

+ Info Page: Displays gold price information over the past 15 days and full historical data.

## Installation

+ Clone the repository
+ Navigate to the project directory
+ Install the required Python packages : pip install -r requirements.txt
+ Run migrations: python manage.py migrate
+ Start the development server: python manage.py runserver
+ Open your web browser and go to http://localhost:8000/ to access the Gold Price Prediction Web App.


## Conclusion

 <div align="justify"> The Gold Price Prediction Web App combines data analysis, machine learning, and web development to provide users with insights into gold price trends. It offers a user-friendly interface with interactive visualizations and real-time data integration, making it a valuable tool for anyone interested in gold market analysis. Feel free to explore and customize the application based on your specific needs. </div>



