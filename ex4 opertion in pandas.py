import pandas as pd, numpy as np 
d = {'RollNo.':[501,502,503,504,505,506,507,508,509,510,511,512], 
'Name':['Ram.N.K','Kumar.A','Kavi.S','Malar.M','Seetha.P.','Kishore.L','Amit.M','Daniel.R','Shyam.M.','Priya.N','Mani.R.','Ravi.S'], 
'A8':[92,100,100,100,76,96,100,92,68,52,72,80], 
'A9':[84,95,90,100,42,84,95,100,53,16,53,np.nan], 
'A10':[100,100,94,100,31,81,100,100,94,13,88,6], 
'Asg':[15,13,14,14,13,14,14,14,5,np.nan,np.nan,np.nan], 
'Test':[19,14,19,18,17,19,19,19,18,'-',18,'-']} 
df = pd.DataFrame(d) 
print('Missing values:\n', df.isnull().sum()) 
15  
df['A9'] = df['A9'].fillna(0) 
df['Asg'] = df['Asg'].fillna(df['Asg'].min()) 
df = df.replace('-',0) 
print(df) 
r1 = df[df['A8']>=80] 
r2 = df[(df['A8']<80)&(df['A8']>=70)] 
r3 = df[df['A8']<70] 
print('Above 80:\n',r1) 
print('70 to 80:\n',r2) 
print('Below 70:\n',r3) 
srt = df.sort_values(by='A9', ascending=False) 
print('Sorted Sept Attendance:\n') 
display(srt[['RollNo.','Name','A9']]) 
df['ConsAttend'] = (df['A8']+df['A9']+df['A10'])/3 
print('Consolidated Attendance:\n',df) 
print('Students with max Test marks:\n') 
display(df[df['Test']==df['Test'].max()]) 
mean_asg = df['Asg'].mean() 
print('Students with Asg < Avg:\n') 
display(df[df['Asg']<mean_asg]) 
df['Res'] = df['Asg'] + df['Test'] 
df['Res'] = df['Res'].apply(lambda x: 'Pass' if x>=20 else 'Fail') 
display(df) 
