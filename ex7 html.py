import pandas as pd
import datetime as dt
def get_hl(df):
   df.drop(df.columns[-1], axis=1, inplace=True)
   df["Date"] = pd.to_datetime(df["Date"], format='%d-%B-%Y')
   df.fillna(0, inplace=True)
   s = dt.datetime.strptime('2018-03-31', '%Y-%m-%d')
   e = dt.datetime.strptime('2019-04-01', '%Y-%m-%d')
   df_fy = df[(df["Date"] > s) & (df["Date"] < e)]
   hi = df_fy["High"].max()
   lo = df_fy["Low"].min()
   return hi, lo, df_fy
if __name__ == "__main__":
   df = pd.read_csv("csv_base_sensex_2018to2020.csv")
   hi, lo, df_fy = get_hl(df)
   df_fy.to_csv("sensex_fy2019-20.csv", index=False)
   print("SENSEX High & Low in FY2019-20:", hi, "&", lo)
