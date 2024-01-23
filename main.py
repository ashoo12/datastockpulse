import time
from xlsxwriter import workbook
import requests
import json
from datetime import datetime,timedelta
import pandas as pd
import openpyxl

excel_writer=pd.ExcelWriter('static/fomousstocks.xlsx', engine='xlsxwriter')

# world famous companies stocks
yesterday=datetime.now().date()-timedelta(1)
ten_days_ago=yesterday-timedelta(days=10)
tickers=["AAPL","TSLA","AMZN","MSFT","GOOG"]
combined_df=pd.DataFrame()
for stock in tickers:
    time.sleep(2)
    famous_stocks=f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/{ten_days_ago}/{yesterday}?adjusted=true&sort=asc&limit=120&apiKey=EdtVH7pcs_9629HyYoRwDGMMjwa3rTM9"
    response1=requests.get(famous_stocks)
    content=response1.json()
    print(content)
    df = pd.DataFrame(content['results'])
    df['Trade name']=content['ticker']
    df.to_excel(excel_writer,sheet_name=stock,index=True)
excel_writer._save()


# us local stock market
us_stocks=f"https://api.polygon.io/vX/reference/financials?apiKey=EdtVH7pcs_9629HyYoRwDGMMjwa3rTM9"
response=requests.get(us_stocks)
data=response.json()
df=pd.DataFrame(data['results'])
us_stock_excelfile= 'usstocks.xlsx'
df.to_excel(us_stock_excelfile, index=True)

