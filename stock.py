# This is my business website.
import streamlit as st
import pandas as pd
import requests as rq
import yfinance as yf

# ---- website config ----
st.set_page_config  (page_title='Stock', page_icon=':chart_with_upwards_trend:', layout='wide')
# create a dataframe of symbols
symbols_list = pd.read_csv('datasets/All_Symbols.csv')
stock_data = pd.DataFrame(columns=['symbol','longName', 'sector', 'industry', 'fullTimeEmployees', 'logo_url'])
# ---- create a sidebar ----
st.sidebar.subheader('Pick a stock')
picked_sym = st.sidebar.selectbox(label='symbols', options=symbols_list['Symbol'].unique())
Company = picked_sym
tickerSymbol = Company  # 'INDA'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id', start='2010-3-30', end='2022-3-30')
z = st.sidebar.button(label='save csv')

if z:
    stock_data = stock_data.append({'symbol': tickerData.info['symbol'], 'longName': tickerData.info['longName'],
                                    'sector': tickerData.info['sector'], 'industry': tickerData.info['industry'],
                                    'fullTimeEmployees': tickerData.info['fullTimeEmployees'],
                                    'logo_url': tickerData.info['logo_url']}, ignore_index=True)
    stock_data.to_csv(f'{picked_sym}_data.csv')
#st.sidebar.selectbox(label='stock type', options=symbols_list['Stock Type'].unique())

with st.container():
    #st.subheader('Forcast Stock Markets')
    st.title('Welcome to our stock forcast')
    #print(tickerData.info)
    st.image(tickerData.info['logo_url'])
    st.write(f'The last 5 days statistics of {Company}!')
    st.write(tickerDf.tail(5))
    st.write(f'stock **closing** price of {Company}!')
    st.line_chart(tickerDf.Close)
    #st.line_chart(tickerDf.Volume)
    #tickerDf.to_csv('i.csv')