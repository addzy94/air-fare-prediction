
import pandas
from functions import fare, finals, findDay
# import os
pandas.set_option('display.width', 1920)
pandas.set_option('display.max_rows', 150)
dataframe = pandas.read_csv("D:\\TravelSpends\\flights9.csv")
# dataframe = dataframe.iloc[::2]
# dataframe.to_csv("D:\\TravelSpends\\flights9.csv", index = False)
# dataframe = dataframe[dataframe.uniqueID.notnull()]
# dataframe.to_csv("D:\\TravelSpends\\flights7.csv", index = False)
# numbers = {"AA": 1, "AS": 2, "B6": 3, "DL": 4, "F9": 5, "HA": 6, "NK": 7, "EV": 8, "OO": 9, "UA": 10, "VX": 11, "WN": 12}
# dataframe["CarrierNum"] = dataframe["Carrier"].map(numbers)
# dataframe.to_csv("D:\\TravelSpends\\flights6.csv", index = False)
# for i in range(0, len(dataframe)):
	# dataframe.ix[i, 10] = carrier_numbers(dataframe.ix[i, 3])
# dataframe["uniqueID"] = dataframe["FlightDate"].str[:2] + "_" + dataframe["FlightDate"].str[3:5] + "_" + dataframe["TailNum"] + "_" + dataframe["FlightNum"].map(str)
# print dataframe
# print dataframe["Carrier"].unique()
# print aircarrier("B6")
# del dataframe["TailNum"]
# del dataframe["FlightNum"]
# dataframe.to_csv("D:\\TravelSpends\\flights3.csv", index = False)
# dataframe = pandas.read_csv("D:\\TravelSpends\\flights5.csv")
# dataframe["DepTime"] = dataframe["DepTime"].map(str)
# dataframe["DepTime"] = dataframe["DepTime"].str[:-2] + ":" + dataframe["DepTime"].str[-2:]
# dataframe.to_csv("D:\\TravelSpends\\flights4.csv", index = False)
# print dataframe
# dataframe2 = pandas.DataFrame()
# dataframe2["uniqueID"] = dataframe["uniqueID"]
# for day in range(0, 31):
	# colname = str(day) + "_days_before"
	# dataframe2[colname] = 1
# dataframe2.to_csv("D:\\TravelSpends\\fares.csv", index = False)

# hourAndDay(4, 15, 2, 16)
# dataframe = pandas.read_csv("D:\\TravelSpends\\flights4.csv")
# dataframe.DepTime[dataframe.DepTime[0] == ":"] = "00"
# for value in dataframe["DepTime"]
	# if value[0] == ":"
		# value
# dataframe.DepTime[dataframe.DepTime.str[0] == ":"] = "00" + dataframe["DepTime"]
# dataframe.to_csv("D:\\TravelSpends\\flights5.csv", index = False)

# csv_chunks = pandas.read_csv("D:\\TravelSpends\\fares.csv", chunksize = 10000)
# dataframe2 = pandas.concat(chunk for chunk in csv_chunks)
# print dataframe2

# dataframe2 = pandas.read_csv("D:\\TravelSpends\\fares.csv")

# dataframe = pandas.read_csv("D:\\TravelSpends\\flights5.csv")
# print dataframe.dtypes
# dataframe3 = pandas.DataFrame()
# dataframe3["happy"] = ""
# print dataframe3.dtypes
# dataframe3["happy"] = dataframe3["happy"].astype(float)
# print dataframe3.dtypes
# print dataframe.ix[445826, 0]

# dataframe2 = pandas.read_csv("D:\\TravelSpends\\fares.csv")

# for i in range(0, len(dataframe)):
	# carrier = dataframe.ix[i, 3]
	# dDep = dataframe.ix[i, 2]
	# dist = dataframe.ix[i, 9]
	# ans = fare(carrier, dDep, dist)
	# for j in range(1, len(dataframe2.columns)):
		# daysBef = dataframe2.columns[j][0:2]
		# finans = finals(ans, dDep, daysBef)
		# dataframe2.ix[i, j] = finans
		
# dataframe2.to_csv("D:\\TravelSpends\\farestest.csv", index = False)
# print len(dataframe2)

def func1(str):
    if(len(str) < 2):
        return("0" + str)
    return(str)

dataframe2 = pandas.read_csv("D:\\TravelSpends\\farestest.csv")
dataframe3 = {}
for i in range(0, 31):
    dataframe3[i] = pandas.DataFrame()
    dataframe3[i]["UniqueID"] = dataframe["uniqueID"]
    val = func1(str(i)) + "_days_before"
    dataframe3[i]["Price"] = dataframe2[val]
    dataframe3[i]["Distance"] = dataframe["Dist"]
    dataframe3[i]["CarrierNum"] = dataframe["CarrierNum"]
    dataframe3[i]["Day"] = dataframe["DayNum"]
    dataframe3[i]["DayOfBooking"] = dataframe.apply(lambda row: findDay(row["DayNum"], i), axis = 1)
    name = "D:\\TravelSpends\\MultipleRegressions\\MultipleRegression" + str(i) + ".csv"
    dataframe3[i].to_csv(name, index = False)


