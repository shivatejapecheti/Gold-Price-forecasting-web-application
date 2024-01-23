# views.py
from django.shortcuts import render
import yfinance as yf

def goldpresentprice(request):
    if request.method == 'POST':
        # Get the selected date from the form
        selected_date = request.POST.get('selected_date')

        # ========== READ DATA ==========
        Df = yf.download('GLD', '2008-01-01', '2023-12-31', auto_adjust=True)
        # Only keep close columns
        Df = Df[['Close']]
        # Drop rows with missing values
        Df = Df.dropna()

        try:
            # Filter the DataFrame based on the selected date
            selected_date_data = Df.loc[selected_date]

            # Get the gold price for the selected date
            gold_price = selected_date_data['Close'].item() if not selected_date_data.empty else None

            # Render the template with the gold price
            return render(request, 'GoldPricePrediction/price.html', {'gold_price': gold_price, 'selected_date': selected_date})

        except KeyError:
            # Handle the case where the selected date is not in the DataFrame
            error_message = f"No data available for the entered date ({selected_date})."
            return render(request, 'GoldPricePrediction/price.html', {'error_message': error_message})

    # Render the initial page with the form
    return render(request, 'GoldPricePrediction/price.html', {'gold_price': None, 'error_message': None})
