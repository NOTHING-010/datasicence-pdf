import pandas as pd

def get_irnss_data(url,table):
    data=pd.read_html(url,match=table)
    df=data[0]
    df_sub=df[~df['status'].str.contains('planned')]
    df_sub['Lanch']=pd.to_datetime(df_sub['Lanch Date'],format='%d %B %y')
    
