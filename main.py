import sys
import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

Liliana_paper = pd.read_csv("Liliana_of_the_Veil_[ISD]_paper.csv", names = ["Date", "price"])
Liliana_online = pd.read_csv("Liliana_of_the_Veil_[ISD]_online.csv", names = ["Date", "price"])


dates = Liliana_online.iloc[:,0].copy()
dates2 = Liliana_paper.iloc[:,0].copy()
d1 = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
d2 = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates2]
price_p = Liliana_paper.iloc[:,1].copy()
price_o = Liliana_online.iloc[:,1].copy()

# Correlation coefficient:
correlation = np.corrcoef(price_o[-2100:], price_p[-2100:])[0,1]
print("Pearson correlation = ", correlation)

plt.gca().xaxis.set_major_locator(mdates.YearLocator())
online = plt.plot_date(d1, price_o, 'r-', label = "Online price")
paper = plt.plot_date(d2, price_p, 'b-', label = "Paper price")
plt.legend(loc='upper left')
plt.title("Prices for card [Liliana of the Veil]")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
