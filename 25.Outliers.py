#24)How to handle outliers.
import pandas as pd
import numpy as np

df=pd.read_csv(r'D:\itvedant\Vscode\Salary_dataset.csv')
df.head()
df[df['col']>2000].index              # it gives list of index 
df.drop(index=['list of outliers'])