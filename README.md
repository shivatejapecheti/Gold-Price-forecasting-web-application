# Gold-Price-forecasting-web-application

 <div align="justify"> The Gold Price Prediction Web App is a Django-based application that leverages machine learning techniques to predict gold prices. This detailed overview provides insights into the methodologies, features, technologies used, and the functionality of the application. </div>

 [Presentation](https://www.canva.com/design/DAF4tbnq1iY/nN6byRnGjQQlbrBdkqAH0A/edit?utm_content=DAF4tbnq1iY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
 
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

The goal of this project was to develop a robust predictive analytics model for forecasting gold ETF prices and implementing a simulated trading strategy based on these predictions. By leveraging historical financial data and advanced machine learning techniques, the aim was to create a reliable system for informed financial decision-making and optimization of trading strategies.

Achievements
+ Historical Data Utilization: Successfully collected and processed historical price data of Gold ETFs (GLD) from Yahoo Finance, ensuring data integrity and relevance for model training and evaluation.

Feature Engineering:

+ Created explanatory variables by calculating short-term (3-day) and medium-term (9-day) moving averages of closing prices.
+ These features were essential for improving the model's predictive accuracy.
  
Predictive Modeling:

+ Developed and trained a Linear Regression model using the engineered features to predict the next day's closing prices of Gold ETFs.
+ Achieved a robust regression model with an interpretable formula: "Gold ETF Price (y) = %.2f * 3 Days Moving Average (x1) + %.2f * 9 Days Moving Average (x2) + %.2f (constant)".
  
Prediction Accuracy:

+ Evaluated the model's performance on a test dataset, achieving an R² score of %.2f, indicating a significant portion of the variance in the target variable explained by the model.

Visualization and Analysis:
+ Plotted the historical closing prices and the predicted vs. actual prices of Gold ETFs, facilitating a clear visual comparison and validation of the model’s performance.
+ Generated interactive plots using Plotly for enhanced data visualization and analysis.
  
Trading Strategy Simulation:

+ Implemented a predictive model-based trading strategy, generating buy signals when the predicted price was expected to rise.
+ Calculated and visualized the cumulative returns of the strategy, demonstrating its potential effectiveness in a real-world trading scenario.
  
Performance Metrics:

+ Assessed the strategy's performance with key metrics such as cumulative returns and the Sharpe ratio, achieving a Sharpe ratio of %.2f, which indicates a favorable risk-adjusted return.
  
Technical Stack:

Utilized a comprehensive set of libraries and frameworks including Django for web development, scikit-learn for machine learning, pandas and NumPy for data manipulation, yfinance for data retrieval, and Plotly for interactive data visualization.

Key Concepts and Terminology:
+ Predictive Analytics: Using statistical and machine learning techniques to make predictions about future outcomes based on historical data.
+ Machine Learning: Training algorithms to recognize patterns and make decisions based on data.
+ Linear Regression: A statistical method for modeling the relationship between a dependent variable and one or more independent variables.
+ Moving Average: A calculation to analyze data points by creating a series of averages of different subsets of the full data set.
+ R² Score: A statistical measure that indicates how well data fit a regression model.
+ Cumulative Returns: The total return of an investment over a period of time, considering reinvestment of dividends and capital gains.
+ Sharpe Ratio: A measure of the risk-adjusted return of an investment portfolio.
+ Buy Signal: An indication generated by a trading strategy to purchase a security based on predicted future price increases.
+ No Position Signal: An indication to hold off on buying or selling a security based on predicted price stability or decline.
+ This comprehensive approach demonstrates the successful application of predictive analytics, data science, and machine learning techniques in developing a predictive model and implementing a trading strategy for gold ETF prices.



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


## Citation

If you find this work useful for your research or project, please consider citing it. 
