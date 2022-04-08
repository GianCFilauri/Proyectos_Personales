import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf

amzn = yf.Ticker("AMZN")
#print(amzn.info)
#hist =  amzn.history(period="max")
#hist = amzn.history(str = "1d", start = "2020-01-01", end = "2022-02-28")
hist = amzn.history(interval = "1d", start = "2022-01-01", end = "2022-01-10")
hist5 = amzn.history(interval = "5d", start = "2022-01-01", end = "2022-01-10")
print(hist)
print(hist5)
#recomend = amzn.recommendations
#print(recomend)