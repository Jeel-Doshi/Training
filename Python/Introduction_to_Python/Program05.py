#Program to extract year, month, date and time using lambda

import datetime

current_status = datetime.datetime.now()

fun = lambda current_status:print(current_status)

print("Year",end=' ')
fun(current_status.year)
print("Month",end=' ')
fun(current_status.month)
print("Day",end=' ')
fun(current_status.day)
print("Time",end=' ')
fun(current_status.timestamp())


