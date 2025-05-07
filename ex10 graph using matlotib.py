import statsmodels.api as sm 
import matplotlib.pyplot as plt 
df = sm.datasets.copper.load_pandas().data 
fig = plt.figure(figsize=(10, 5)) 
ax1 = plt.subplot(2, 1, 1) 
ax2 = plt.subplot(2, 1, 2) 
x = range(1951, 1975 + 1) 
ax1.plot(x, df["COPPERPRICE"], color='orange', ls='--') 
ax1.set(xlabel='Time', ylabel='Copper price', title="Copper & Aluminum Price") 
ax2.plot(x, df["ALUMPRICE"], color='blue', ls='-.') 
ax2.set(xlabel='Time', ylabel='Aluminum price') 
plt.show()
