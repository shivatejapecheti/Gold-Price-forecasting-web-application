from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from login.views import *

#========== IMPORT LIBRARIES ==========
from sklearn.linear_model import LinearRegression

import pandas as pd
import numpy as np
# Turn off pandas warning
pd.set_option('mode.chained_assignment', None)

# For Getting Dataset From YahooFinance
import yfinance as yf



# Get today's date
from datetime import datetime, timedelta
import pytz
today = datetime.now(tz=pytz.timezone('US/Eastern')).strftime('%Y-%m-%d')

# For Graphs
import plotly.offline as opy
from plotly.graph_objs import Scatter
import plotly.graph_objects as go

#========== READ DATA ==========
Df = yf.download('GLD', '2008-01-01', today, auto_adjust=True)
# Only keep close columns
Df = Df[['Close']]
# Drop rows with missing values
Df = Df.dropna()

print(Df.head())

# Plot the closing price of GLD
x_data = Df.index
y_data = Df['Close']
ClosingPricePlot_div = opy.plot({
    'data': [Scatter(x=x_data, y=y_data, mode='lines', name='test', opacity=0.8, marker_color='green')],
    'layout': {'title': 'Gold ETF Price Series', 'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Gold ETF price (in $)'}}
}, output_type='div')

#========== DEFINE EXPLANATORY VARIABLES ==========
Df['S_3'] = Df['Close'].rolling(window=3).mean()
Df['S_9'] = Df['Close'].rolling(window=9).mean()
Df['next_day_price'] = Df['Close'].shift(-1)

Df = Df.dropna()
X = Df[['S_3', 'S_9']]

# Define dependent variable
y = Df['next_day_price']

#========== TRAIN AND TEST DATASET ==========
t = .8
t = int(t*len(Df))

# Train dataset
X_train = X[:t]
y_train = y[:t]

# Test dataset
X_test = X[t:]
y_test = y[t:]

#========== LINEAR REGRESSION MODEL ==========
linear = LinearRegression().fit(X_train, y_train)
RegressionModelFormula = "Gold ETF Price (y) = %.2f * 3 Days Moving Average (x1) + %.2f * 9 Days Moving Average (x2) + %.2f (constant)" % (linear.coef_[0], linear.coef_[1], linear.intercept_)

#========== PREDICTING GOLD ETF PRICES ==========
predicted_price = linear.predict(X_test)
predicted_price = pd.DataFrame(predicted_price, index=y_test.index, columns=['price'])
# Attach y_tese series to dataframe
predicted_price['close'] = y_test
# Plot graph
x_data = predicted_price.index
y_data_predicted = predicted_price['price']
y_data_actual = predicted_price['close']
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_data, y=y_data_predicted,
                    mode='lines',
                    name='Predicted Price'))
fig.add_trace(go.Scatter(x=x_data, y=y_data_actual,
                    mode='lines',
                    name='Actual Price'))
PredictionPlot_div = opy.plot({
    'data': [Scatter(x=x_data, y=y_data_predicted, mode='lines', name='Predicted Price', opacity=0.8),
    Scatter(x=x_data, y=y_data_actual, mode='lines', name='Actual Price', opacity=0.8)],
    'layout': {'title': 'Predicted VS Actual Price', 'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Gold ETF price (in $)'}}
}, auto_open=False, output_type='div')

#========== CUMULATIVE RETURNS ==========
gold = pd.DataFrame()

gold['price'] = Df[t:]['Close']
gold['predicted_price_next_day'] = predicted_price['price']
gold['actual_price_next_day'] = y_test
gold['gold_returns'] = gold['price'].pct_change().shift(-1)
    
gold['signal'] = np.where(gold.predicted_price_next_day.shift(1) < gold.predicted_price_next_day,1,0)
    
gold['strategy_returns'] = gold.signal * gold['gold_returns']
x_data = gold.index
y_data = ((gold['strategy_returns']+1).cumprod()).values
CumulativeReturns_div = opy.plot({
    'data': [Scatter(x=x_data, y=y_data, mode='lines', name='test', opacity=0.8, marker_color='green')],
    'layout': {'title': 'Cumulative Returns', 'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Cumulative Returns (X 100%)'}}
}, output_type='div')

#========== PREDICT DAILY MOVES ==========
data = yf.download('GLD', '2008-06-01', today, auto_adjust=True)
data['S_3'] = data['Close'].rolling(window=3).mean()
data['S_9'] = data['Close'].rolling(window=9).mean()
data = data.dropna()
data['predicted_gold_price'] = linear.predict(data[['S_3', 'S_9']])
data['signal'] = np.where(data.predicted_gold_price.shift(1) < data.predicted_gold_price,"Buy","No Position")


# Return to Context functions
def PlotClosingPrice():
    return ClosingPricePlot_div

def RegressionModel():
    return RegressionModelFormula

def PredictionPlot():
    return PredictionPlot_div

def r2_scoreCalculate():
    # R square
    r2_score = linear.score(X[t:], y[t:])*100
    r2_score = float("{0:.2f}".format(r2_score))
    return r2_score

def CumulativeReturns():
    return CumulativeReturns_div

def SharpeRatioCalculate():
    return '%.2f' % (gold['strategy_returns'].mean()/gold['strategy_returns'].std()*(252**0.5))

def MovingAverage_S3():
    return round(data['S_3'].iloc[-1], 2)

def MovingAverage_S9():
    return round(data['S_9'].iloc[-1], 2)

def GetSignal():
    return data['signal'].iloc[-1]

def GetPredictedPrice():
    return round(data['predicted_gold_price'].iloc[-1], 2)

def GetNextDay():
    NextDate = (data.index[-1].date() + timedelta(days=1)).strftime('%d/%m/%Y')
    return NextDate

def GetClosingPrice():
    return round(data["Close"].iloc[-1], 2)

def GetClosingPriceDate():
    return data.index[-1].strftime("%d/%m/%y")

#Ended
# @login_required
def home(request):
    #Added

    context = {
        'ClosingPricePlot_div' : PlotClosingPrice(),
        'PredictionPlot_div' : PredictionPlot(),
        'CumulativeReturns_div' : CumulativeReturns(),
        'SharpeRatio' : SharpeRatioCalculate(),
        'S_3' : MovingAverage_S3(),
        'S_9' : MovingAverage_S9(),
        'Signal' : GetSignal(),
        'PredictedPrice' : GetPredictedPrice(),
        'NextDate' : GetNextDay(),
        'ClosingPrice' : GetClosingPrice(),
        'ClosingDate' : GetClosingPriceDate(),
    }

    #Ended
    return render(request, 'GoldPricePrediction/home.html', context)

# def base(request):
#     return render(request, 'GoldPricePrediction/base.html')

def information(request):
    context = {
        'RegressionModelFormula' : RegressionModel(),
        'r2_score' : r2_scoreCalculate(),
    }
    return render(request, 'GoldPricePrediction/information.html', context)


def plots_view(request):
    context = {
        'ClosingPricePlot_div' : PlotClosingPrice(),
        'PredictionPlot_div' : PredictionPlot(),
        'CumulativeReturns_div' : CumulativeReturns(),
        'SharpeRatio' : SharpeRatioCalculate(),
        'S_3' : MovingAverage_S3(),
        'S_9' : MovingAverage_S9(),
        'Signal' : GetSignal(),
        'PredictedPrice' : GetPredictedPrice(),
        'NextDate' : GetNextDay(),
        'ClosingPrice' : GetClosingPrice(),
        'ClosingDate' : GetClosingPriceDate(),
    }

    # Your logic to generate content for the 'plots' page
    # For example, rendering a template named 'plots.html'
    return render(request, 'GoldPricePrediction/plots.html',context )



import requests
from django.shortcuts import render, redirect

def gold_price(request):
    api_key = 'goldapi-11lmmjrlpvgste1-io'  # Replace 'YOUR_API_KEY_HERE' with your actual API key
    gold_api_url = 'https://www.goldapi.io/api/XAU/USD'
    headers = {'x-access-token': api_key}

    try:
        response = requests.get(gold_api_url, headers=headers)
        if response.status_code == 200:
            gold_data = response.json()
            gold_price = gold_data['price']
            context = {'gold_price': gold_price}
            return render(request, 'GoldPricePrediction/gold_price.html', context)

    except requests.RequestException as e:
        print(f"API Error: {e}")
    
    # In case of error or failure, redirect to home page or display an error message
    return redirect('home')  # Redirect to home page if there's an error








from django.shortcuts import render
from django.http import HttpResponse

# Function to set a cookie
def set_cookie(request):
    response = render(request, 'GoldPricePrediction/home.html')
    # Set a cookie named 'gold_prediction' with a value
    response.set_cookie('gold_prediction', 'predicted_value')
    return response


from django.shortcuts import render
from django.http import HttpResponse

# Function to get a cookie
def get_cookie(request):
    # Get the value of the 'gold_prediction' cookie
    predicted_value = request.COOKIES.get('gold_prediction')
    return HttpResponse(f'Predicted value from cookie: {predicted_value}')

# Include this function in your views where needed








from django.http import HttpResponse

def set_user_timezone(request):
    # Get user's preferred timezone (for example, let's assume 'US/Eastern')
    user_timezone = 'US/Eastern'  # You might fetch this from user settings

    response = render(request, 'GoldPricePrediction/home.html')

    # Set 'user_timezone' cookie with the user's preferred timezone
    response.set_cookie('user_timezone', user_timezone)

    return response

def get_user_timezone(request):
    # Retrieve 'user_timezone' cookie value
    user_timezone = request.COOKIES.get('user_timezone')

    return HttpResponse(f"User's Timezone: {user_timezone}")


def info_page(request):
    # Add any context data or logic needed to render Info.html
    return render(request, 'GoldPricePrediction/info.html')


def info_page(request):
    # Fetch gold price data from your database or an API
    # Example data - modify this with your actual data retrieval
    gold_prices = [
        {'date': '2023-12-01', 'price': 1500},
        # ... (Fetch data for other dates)
    ]

    # Send data to the template
    context = {
        'gold_prices': gold_prices,
        # Add other context data needed for your page
    }
    return render(request, 'GoldPricePrediction/info.html', context)


# =======================================


# Function to get gold price data for the graph and table
def gold_price_view(request):
    # Retrieve data from Yahoo Finance from December 1st, 2023, to current date
    gold_data = yf.download('GOLD', start='2023-12-01', end=datetime.now().strftime('%Y-%m-%d'), progress=False)
    
    # Process the data to format for the graph
    gold_prices = [{'date': str(index.date()), 'price': price} for index, price in zip(gold_data.index, gold_data['Close'])]

    # Retrieve data for the past 15 days for the table
    past_15_days = gold_data.tail(15)
    past_15_days_data = [{'date': str(index.date()), 'price': price} for index, price in zip(past_15_days.index, past_15_days['Close'])]

    return render(request, 'GoldPricePrediction/info.html', {'gold_prices': gold_prices, 'past_15_days': past_15_days_data})


from datetime import datetime, timedelta
import yfinance as yf

def info_page(request):
    # Fetch gold price data from Yahoo Finance for the past 15 days
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d')
    
    gold_data = yf.download('GLD', start=start_date, end=end_date, progress=False)
    gold_prices_past_15_days = gold_data['Close'].reset_index().tail(15).values.tolist()

    # Fetch gold price data from Yahoo Finance from 2023-12-01 to the current date for the graph
    gold_data_full = yf.download('GLD', start='2023-12-01', end=end_date, progress=False)
    gold_prices_full = gold_data_full['Close'].reset_index().values.tolist()

    context = {
        'gold_prices_past_15_days': gold_prices_past_15_days,
        'gold_prices_full': gold_prices_full,
    }
    return render(request, 'GoldPricePrediction/info.html', context)









# def login_page(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('home')  # Redirect to home page after successful login
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})




# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         User.objects.create(username=username, password=password)
#         # Here, you might want to add authentication logic
#         # For simplicity, this example just saves the user directly to the database
#         return redirect('home')  # Redirect to the home page after login

#     return render(request, 'login.html')