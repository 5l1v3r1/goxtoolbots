import datetime
import time
import pickle
import sqlite3
import calendar
import math
from indicator.ma import ExponentialMovingAverage as ema
from indicator.ma import SimpleMovingAverage as sma
from indicator.candlestick import CandleStick
from indicator.timesum import TimeSum
from exchange_connection import ExchangeConnection, MockExchangeConnection
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as pltdates

class StrategyPlot:

	def __init__(self, debugData, numberSubplots):
		self.debugData = debugData
		self.numberSubplots = numberSubplots
		self.xfrom = None
		self.xto = None

		# Get the right x scale
		time = []
		for item in debugData["RawPrice"]:
			time.append( datetime.datetime.fromtimestamp(item["now"]) )
		self.SetXLimits(time[0], time[-1])

	def SetXLimits(self, xfrom, xto):
		self.xfrom = xfrom
		self.xto = xto

	def Plot(self, plotName, subplot, format="r-"):

		if (plotName not in self.debugData):
			return

		time = []
		value = []
		for item in self.debugData[plotName]:
			time.append( datetime.datetime.fromtimestamp(item["now"]) )
			value.append(item["value"])

		plt.subplot(self.numberSubplots,1,subplot)
		plt.plot(time, value, format)
		plt.ylabel(plotName)
		if ( (self.xfrom != None) and (self.xto != None) ):
			plt.xlim([self.xfrom, self.xto])

	def Show(self):
		plt.show()
