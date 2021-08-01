from random import uniform

def aircarrier(carrier):
	prices = {"AA": 1, "AS": 1.2, "B6": 1.6, "DL": 0.85, "F9": 1.22, "HA": 0.75, "NK": .66, "EV": 1.5, "OO": 1, "UA": 1.14, "VX": 0.90, "WN": 1.25}
	return prices[carrier]

def carrier_numbers(carrier):
	numbers = {"AA": 1, "AS": 2, "B6": 3, "DL": 4, "F9": 5, "HA": 6, "NK": 7, "EV": 8, "OO": 9, "UA": 10, "VX": 11, "WN": 12}
	return numbers[carrier]
	
def findDay(currDay, beforeDay):
	beforeDay = int(beforeDay)
	beforeDay = beforeDay % 7
	if((currDay - beforeDay) > 0):
		dayAns = currDay - beforeDay;
	else:
		dayAns = 7 - abs(currDay - beforeDay)
	return(dayAns)

def distanceCalc(dist):
	if(dist < 1000):
		val = dist * .45
	else:
		val = (dist * .45) + (dist - 1000) * .65
	return(val)
		
def dayOfBooking(day):
	val  = -0.00208333 * pow(day, 6) + 0.0520833 * pow(day, 5) - 0.516667 * pow(day, 4)
	val = val  + 2.57708 * pow(day, 3) - 6.70625 * pow(day, 2) + 8.34583 * day - 2.5
	return(round(val  + uniform(0.01, 0.1), 2))
	
def daysBefore(days):
	days = int(days)
	val = (1125 - pow(days, 2)) * .15
	return(round(val  + uniform(0.01, 0.1), 2))


def dayOfDeparture(day):
	val = 0.00409722 * pow(day, 6) - 0.091875 * pow(day, 5) + 0.792014 * pow(day, 4)
	val = val - 3.29896 * pow(day, 3) + 6.87889 * pow(day, 2) - 6.73417 * day + 3.65
	return(round(val, 2))
	
def fare(carrier, dayOfDep, distance):
	finalFare = aircarrier(carrier) * .15 + distanceCalc(distance) * .25;
	finalFare = finalFare + dayOfDeparture(dayOfDep) * .10
	return(finalFare)

def finals(prevfare, dayOfDep, daysBef):
	finalfare = prevfare + daysBefore(daysBef) * .15;
	finalfare = finalfare + dayOfBooking(findDay(dayOfDep, daysBef)) * 3 + uniform(0, 5)
	return (round(finalfare, 2))