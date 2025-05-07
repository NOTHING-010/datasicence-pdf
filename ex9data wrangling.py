import pandas as pd 
import numpy as np 
def get_model(df): 
   m_mean = pd.pivot_table(df, values=["MYCT", "MMIN", "MMAX", "CACH", "CHMIN", "CHMAX", 
"PRP"],columns="vendor name", aggfunc=np.mean) 
   m_median = pd.pivot_table(df, values=["MYCT", "MMIN", "MMAX", "CACH", "CHMIN", "CHMAX", 
"PRP"], columns="vendor name", aggfunc=np.median) 
   df_mean_myct = pd.DataFrame({"vendor name": list(m_mean.columns), "Mean MYCT": 
   m_mean.values.tolist()[5]}) 
   m_models = pd.melt(df, id_vars=["vendor name"], value_vars=["Model Name"]) 

   m_myct = pd.melt(df_mean_myct, id_vars=["vendor name"], value_vars=["Mean MYCT"]) 
   result = pd.concat([m_models, m_myct], ignore_index=True) 
   return result 
if __name__ == "__main__": 
   df_input = pd.read_csv("D:\py promg\dataset\computer+hardware\machine.data", header=None, names=["vendor name", "Model Name", 
"MYCT", "MMIN", "MMAX", "CACH", "CHMIN", "CHMAX", "PRP", "ERP"]) 
   result = get_model(df_input) 
   print(result)
