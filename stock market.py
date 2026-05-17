# create a python series
import pandas as pd
stock_prices= pd.Series([3520.40, 1478.90, 1620.55, 2780.30, 425.60, 1023.75, 2610.15],index= ['TCS', 'Infosys', 'HDFC Bank', 'Reliance', 'Wipro', 'ICICI Bank', 'HUL'])
print(stock_prices)

# greater then 1500
a=stock_prices[stock_prices>1500]
print(a)

#min stock and max stock
 
max_stockname= stock_prices.idxmax()
max_stockprice=stock_prices.max()

min_stockname=stock_prices.idxmax()
min_stockprice= stock_prices.max()

print("maximum stock name =>",max_stockname, "\n minimum stock name =>",min_stockname,"\nMaximim stock price=>", max_stockprice,"\n Minimum stock price=>",min_stockprice)
