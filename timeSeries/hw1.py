import pandas as pd

fileName = 'EE627A_HW1_Data_Python.csv'
df = pd.read_csv(fileName)

#Method of correlation: Pearson 
#.loc uses label based indexing
#First parameter searches all rows starting with 'food' ends in 'other'
#Second parameter searches all columns starting with 'Mkt-RF (Market-risk free)' ends with 'Momentum'

correlation = df.corr().loc['Food':'Other', 'Mkt-RF (Market-risk free)':'Momentum']

#Save five factor returns
five_factors = df.loc[:,'Mkt-RF (Market-risk free)':'Momentum'] 
expected_value = five_factors.mean()

#Create time series for five factors, then compute auto correlation with lag 

MKTRF_Series = df.loc[:,'Mkt-RF (Market-risk free)']
SMB_Series = df.loc[:,'SMB (Small minus big)']
HML_Series = df.loc[:,'HML (High minus low)']
RF_Series = df.loc[:,'RF (Risk free rate)']
Momentum_Series = df.loc[:,'Momentum']

autocorr = pd.DataFrame({'Mkt-RF (Market-risk free)': [], 'SMB (Small minus big)': [], 'HML (High minus low)': [],'RF (Risk free rate)': [], 'Momentum': []})

for i in range(11):
     autocorr = autocorr.append({'Mkt-RF (Market-risk free)': MKTRF_Series.autocorr(lag=i), 'SMB (Small minus big)': SMB_Series.autocorr(lag=i), 'HML (High minus low)': HML_Series.autocorr(lag=i),'RF (Risk free rate)': RF_Series.autocorr(lag=i), 'Momentum': Momentum_Series.autocorr(lag=i)}, ignore_index = True)


print(correlation)
print('\n1. Mkt-RF correlates most highly with every industry')
print('2. Momentum correlates negatively with each industry')
print('3. RF does not correlate highly with the 30 industry time series. In fact it is weakly correlated\n')
print(autocorr)