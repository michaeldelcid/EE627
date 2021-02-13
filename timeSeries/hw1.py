import pandas as pd

fileName = 'EE627A_HW1_Data_Python.csv'
df = pd.read_csv(fileName)

#Method of correlation: Pearson 
#.loc uses label based indexing
#First parameter searches all rows starting with 'food' ends in 'other'
#Second parameter searches all columns starting with 'Mkt-RF (Market-risk free)' ends with 'Momentum'

correlation = df.corr().loc['Food':'Other', 'Mkt-RF (Market-risk free)':'Momentum']
print(correlation)

print('\n1. Mkt-RF correlates most highly with every industry')
print('2. Momentum correlates negatively with each industry')
print('3. RF does not correlate highly with the 30 industry time series. In fact it is weakly correlated')