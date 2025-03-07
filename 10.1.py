import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
unique_values = data['whoAmI'].unique() 
one_hot = pd.DataFrame()
for value in unique_values:
    one_hot[value] = (data['whoAmI'] == value).astype(int)
data = pd.concat([data, one_hot], axis=1)
print(data.head())