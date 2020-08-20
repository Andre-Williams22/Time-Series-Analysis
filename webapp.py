import streamlit as st 
import pandas as pd 
import yfinance as yf

#streamlit run webapp.py

st.write("""
# Simple Stock Market Price App
**Visually** show data on a stock! 
""")

# # Create a sidebar header 
# st.sidebar.header('User Input')

# # Create a function to get the users input 
# def get_input():
#     start_date = st.sidebar.text_input("Start Date", "2020-01-02")
#     end_date = st.sidebar.text_input("End Date", "2020-08-08")
#     stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
#     return start_date, end_date, stock_symbol 

# # function for grabbing company name 
# def get_company_name(symbol):
#     pass


# # get the proper company data and proper timeframe form the user start and end date 
# def get_data(symbol, start, end):
#     symbol = symbol.upper()
#     tickerData = yf.Ticker(symbol)
#     tickerDf = tickerData.history(period='1d', start=start, end=end)



# # get users input 
# start, end, symbol = get_input()
# # get data
# df = get_data(symbol, start, end)

# # get the company name 
# company_name = get_data(symbol.upper())

# # display the close price 
# # st.header(company_name+" Close Price\n")
# # st.line_chart()

# # Display the volume 
# st.header(company_name," Volume\n")


#define the ticker symbol
tickerSymbol = 'CAKE'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2001-5-31', end='2020-08-08')
#Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)