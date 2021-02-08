# Part 1

- Download the monthly time series consisting of returns on:
     - 30 industry (Food, Beer, Smoke, etc)
     - Market-free risk (M-r)
     - SMB (Small minus big)
     - HML (High minus low)
     - RF (risk free rate)
     - Momentum 

- Form the correlation matrix between all these time series. For the four-factor model (market-RF, SMB, HML, and Momentum), which factor correlates most highly with every industry? Which factor correlates negatively with every industry? Does RF (Riskfreerate) correlate highly with 30 industry time series? 

- Form the auto-correlation funcction (ACF) for time-lag 1 to time-lag 10 with the four-factor time series (market-RF, SMB, HML, and Momentum). Is there any AR(1) model in the 4 time series. Explain your observations.

# Part 2 

Suppose that the daily value of a financial time series follows the model: 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**X<sub>t</sub> = 0.01 + 0.2 X<sub>t-2</sub> + &alpha;<sub>t</sub>**

where **{&alpha;<sub>t</sub>}** is a Gaussian white noise series with mean zero and variance 0.02.

- What are the mean and variance of the return series **X<sub>t</sub>**?
- Compute the lag-1 and lag-2 autocorrelation of **X<sub>t</sub>**.
- Assume that **X<sub>100</sub> = -0.01**, and **X<sub>99</sub> = 0.02**. Compute the 1- and 2-step ahead of forecasts of the return series at the forecast origin **t = 100**

 
