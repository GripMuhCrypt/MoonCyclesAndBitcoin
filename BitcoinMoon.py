#moon cycle(s)

#import libraries
from matplotlib import pyplot as plt
import numpy as np
import math

import json
import requests

##locs, labels = xticks()  

#######################################Collect lunar variables
Year = int (input("type year start"))
Month = int(input("what month homie?"))
Day = int(input("It's the first of the month aka DAY plz sir"))
###################################################Calculate data from inputs
#A=Y/100
A = Year/100
#B=A/4
B = A/4  
#C=2-A+B
C = 2-A+B
#E=365.25*(Y + 4713)
E =365.25*(Year + 4713)
#F= 30.6001*(M+1)
F = 30.6001*(Month +1)
#JD= C+D+E+F-1524.5
JD = C + Day + F + E -1524.5
#(DaysSinceNew) = JD-2451549.5
DaysSinceNew = JD - 2451549.5
#NewMoons = (DaysSinceNew)/29.53
NewMoonsSince = DaysSinceNew/29.53
#DROP whole number and multiply by fraction from NewMoons by 29.53 this gives us the how many days into the current moons cylce
CurrentDaysIntoCycle = (NewMoonsSince%1)*29.53
#############################################calulate cycles since given year,m,d
#print(CurrentDaysIntoCycle)
###########################################################################################################
# get info
Request = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=max')
###################################SORT JSON
#convert from to dict type
Dictionary = json.loads(Request.text)
#convert data down to array
arrayData = Dictionary['prices']
#get array info
MAX = len(arrayData)
MIN = 0
##########################################API Data
##sort for graph
#Xar
x1 = [0]*MAX
x2 = np.array(x1)
indexX = 0
while( indexX < MAX):
   x2[ indexX ] = indexX
   indexX += 1
#Yar
y1 = [0]*MAX
y2 = np.array(y1)
indexY = 0
MA = [0]*MAX
#fill array with values for Y @ X
while ( indexY < MAX):
   y2[ indexY ] = arrayData[ indexY ][1]
   if indexY >= 1:
      average = (y2[ indexY ]+y2[ indexY-1 ])/indexY
   if indexY >= 200 :
      MA[indexY] = 
   indexY += 1
#################

###########################################################################################################
#create an Y variable to represnt days since 2012 or some time line format that best fits data set
###############################
y = 0
yArray = [0]*int(DaysSinceNew)
Yarr = np.array(yArray)
###############################
xArray = [0]*int(DaysSinceNew)
Xarr = np.array(xArray)
x = 0
###############################
#create a Y variable to represent a fraction from 0 to 1
while (y < int(DaysSinceNew )): #actual Y variable
    Yarr[y] = ((y/29.53)%1)*29.5
    y += 1
'''
###########################################################################Plot data 1
plt.plot(np.arange(0, int(DaysSinceNew)),Yarr[0:int(DaysSinceNew)] )
#xticks(np.arange(0, DaysSinceNew, step=5))
plt.xlabel("days")
plt.ylabel("moon phase")
plt.title('Moon Cycles')
plt.show()
###########################################################################Plot data 2
plt.plot(np.arange(0,MAX), y2)
plt.xticks(np.arange(0, MAX, step=1))
plt.xlabel("days")
plt.ylabel("price")
plt.title('BTC')
plt.show()
'''
#########################New Plot
##REference:https://www.geeksforgeeks.org/matplotlib-pyplot-twinx-in-python/
fig, ax1 = plt.subplots()

blue = 'tab:blue'
ax1.set_xlabel( 'days')
ax1.set_ylabel( 'moon cycle', color = blue)
ax1.plot( np.arange(0, int(DaysSinceNew)), Yarr, color = blue)
ax1.tick_params( axis = 'y', labelcolor = blue)

ax2 = ax1.twinx()

green = 'tab:green'
ax2.set_ylabel('btc', color = green)
ax2.plot( x2, y2, color = green)
ax2.set_yscale('log')
ax2.tick_params(axis = 'y', labelcolor = green)

ax3 = ax1.twinx()

red = 'tab:red'
ax3.set_ylabel('200 MA', color = red)
ax3.plot( x2, MA, color = red)
ax3.set_yscale('log')
ax3.tick_params(axis = 'y', labelcolor = red)

plt.show()
