from scipy.stats import ttest_1samp
import numpy as np
def t_test(val):
 h = np.array([165, 170, 160, 154, 175, 155, 167, 177, 158, 178])
 print(h)
 mean_h = np.mean(h)
 print('Mean Height =', mean_h)
 t_stat, p = ttest_1samp(h, val)
 print('p-value =', p)
 
 if p < 0.05:
   res = 'Reject null hypothesis'
 else:
    res = 'Accept null hypothesis'
 return res

if __name__ == "__main__":
   val = 160
   res=t_test(val)
   print(res)
   
