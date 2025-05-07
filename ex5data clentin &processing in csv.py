import pandas as pd 
 
def calc_gf(df): 
    if df.isnull().values.any(): 
        print("Detected NaN, replacing with 0") 
        df.fillna(0) 
    else: 
        df.drop(columns=['G3'], inplace=True) 
        df.insert(len(df.columns), 'Gfinal', '') 
        df['Gfinal'] = (df['G1'] + df['G2']) * 100 / 40 
    pass_50 = df[df['Gfinal'] >= 50] 
    below_50 = df[df['Gfinal'] < 50] 
    return pass_50, below_50 
 
if __name__ == "__main__": 
    df = pd.read_csv("student-mat.csv", delimiter=";") 
    pass_50_df, below_50_df = calc_gf(df) 
   
    pass_50_df.to_csv("result_50plus.csv",sep=',', index=False) 
    below_50_df.to_csv("result_below50.csv",sep=',', index=False)
