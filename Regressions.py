import pandas as pd
#import numpy as np
import statsmodels.api as sm
#from mpl_toolkits.mplot3d import Axes3D
from statsmodels.api import add_constant
from functions import fare, finals, findDay, carrier_numbers

#df = pd.read_csv("D:\\TravelSpends\\flights9.csv")
df2 = {}
fit = {}
for i in range(0, 31):
    name = "D:\\TravelSpends\\MultipleRegressions\\MultipleRegression"
    name = name + str(i) + ".csv"
    df2[i] = pd.read_csv(name)
    X = df2[i][['Distance', 'CarrierNum', 'Day', 'DayOfBooking']]
    Y = df2[i]['Price']
    X = add_constant(X)
    fit[i] = sm.OLS(Y, X).fit()

predicted_price = {}
calculated_price = {}
dist = 780
carrier = "HA"
dDep = 7
ans = fare(carrier, dDep, dist)

for i in range(0, 31):
    v0 = fit[i].params[0]
    v1 = dist * fit[i].params[1]
    v2 = carrier_numbers(carrier) * fit[i].params[2]
    v3 = dDep * fit[i].params[3]
    v4 = findDay(dDep, i) * fit[i].params[4]
    predicted_price[i] = v0 + v1 + v2 + v3 + v4
    calculated_price[i] = finals(ans, dDep, i)
#    print("Predicted for day", i, predicted_price[i])
#    print("Calculated for day", i, calculated_price[i])

x = []
pred = []
calc = []
for i in range(0, 31):
    x.append(i)
    pred.append(predicted_price[i])
    calc.append(calculated_price[i])

import matplotlib.pyplot as plt
plt.plot(pred, x)
plt.plot(calc, x)
#t = open("D:\\TravelSpends\\res.txt", "w")
#actuals = 0
#for i in range(0, len(df2)):
#    v0 = fit.params[0]
#    v1 = df2.ix[i, 2] * fit.params[1]
#    v2 = df2.ix[i, 3] * fit.params[2]
#    v3 = df2.ix[i, 4] * fit.params[3]
#    v4 = df2.ix[i, 5] * fit.params[4]
#    inter = v0 + v1 + v2 + v3 + v4 - df2.ix[i, 1]
#    actuals = actuals + abs(inter)
#    print(inter, file = t)
#
#t.close()
#print(actuals / len(df2))

#fig = plt.figure()
#ax = fig.add_subplot(111, projection = '3d')
#ax.scatter(df2['Distance'], df2['DayOfBooking'], df2['Price'], c='r', marker='o')
#xx, yy = np.meshgrid(df2['Distance'], df2['DayOfBooking'])
#ax.set_xlabel('Distance')
#ax.set_ylabel('DayOfBooking')
#ax.set_zlabel('Price')
#plt.show()