from django.http import JsonResponse
from rest_framework.decorators import api_view
import yfinance as yf
import pandas as pd

@api_view(['POST'])
def get_stock_data(request):
    try:
        data = request.data
        ticker = data['ticker']
        # print(data);
        # print(ticker);
        # 数字のみの場合は日本の株式として.Tを付加
        if ticker.isdigit():
            ticker = f"{ticker}.T"
            
        period = data['period']  # 例: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
        
        ticker_data = yf.Ticker(ticker)
        hist = ticker_data.history(period=period)
        # print(hist);
        if hist.empty:
            return JsonResponse({'error': f'No data found for ticker {ticker}'}, status=404)
        
        # DataFrameを整形
        result = hist[['Close']].reset_index()
        result = result.rename(columns={
            'Date': 'date',
            'Close': 'price'
        })
        
        # 日付をISO形式の文字列に変換
        result['date'] = result['date'].dt.strftime('%Y-%m-%d')
        print(result);
        return JsonResponse(result.to_dict(orient='records'), safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)