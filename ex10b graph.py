import statsmodels.api as sm 
import matplotlib.pyplot as plt 
df = sm.datasets.copper.load_pandas().data 
x = range(1951, 1976) 
y1 = df["WORLDCONSUMPTION"].values 
y2 = df["INVENTORYINDEX"].values 
fig, ax1 = plt.subplots(figsize=(15, 8)) 
ax2 = ax1.twinx() 
ax1.bar(x, y1, color='cyan', zorder=2) 
ax1.set_xlabel('Year') 
ax1.set_ylabel('World Consumption (1000 metric tons)') 
ax2.plot(x, y2, 'r-*', label="Inventory Trend", zorder=1) 
33  
ax2.legend(loc="upper left") 
plt.show()
