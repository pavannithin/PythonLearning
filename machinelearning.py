# calculate the Mean(average of all the speed's of a cars)
# average = lambda : print(sum(speed)/len(speed))
# Mean: The sum of all values divided by the count of values (the calculation described above).


import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)



# Median: The middle value of the set when arranged in order from least to greatest.
""""" Link: https://www.google.com/search?q=median+of+numbers&sca_esv=
28031dd5f30059e8&rlz=1C5GCEM_enIN1137IN1137&sxsrf=ANbL-n5FW5MRJxwhjQBw76uoicJOgVxt6A%3A1767853061642&ei=
BUxfaYD2JtizwcsPjbz1sA0&oq=median&gs_lp=Egxnd3Mtd2l6LXNlcnAiBm1lZGlhbioCCAAyChAAGIAEGEMYigUyCxAAGIAEGJECG
IoFMg0QABiABBixAxhDGIoFMgoQABiABBhDGIoFMhAQABiABBixAxhDGIMBGIoFMg0QABiABBixAxhDGIoFMgoQABiABBhDGIoFMgoQABiABBh
DGIoFMgoQABiABBhDGIoFMgoQABiABBhDGIoFSKBiULoDWLoDcAJ4AZABAJgBwxegAcMXqgEDOS0xuAEByAEA-AEC-AEBmAIDoALTF8IC
ChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFmAMAiAYBkAYKkgcFMi44LTGgB6kFsgcDOC0xuAfKF8IHBTAuMS4yyAcLgAgA&sclient=gws-wiz-serp """

speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)




# Mode: The value that occurs most frequently in the set.

# SciPy stands for Scientific Python.

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(f"Mode value of array is {x}")

#The mode() method returns a ModeResult object that contains the mode number (86), and count (how many times the mode number appeared (3)).


# Standard Deviation:
# Standard deviation (SD) measures how spread out numbers in a dataset are from the average (mean); a low SD means data points cluster near the mean
import numpy

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print(f"Standard Deviation {x}")


# Percentiles
# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.


import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(f"75 Percentiles is {x}")


# Data Distribution

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

print(f"Create an array containing 100000 random floats between 0 and 5: {x}")
# bins are nothing but intervals in which data is grouped on x axis
plt.hist(x, 100)
plt.show()


# Normal Data Distribution

# In the previous chapter we learned how to create a completely random array, of a given size, and between two given values.

# In this chapter we will learn how to create an array where the values are concentrated around a given value.

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)
print("Creating a normal distribution:")
plt.hist(x, 100)
plt.show()

# Scatter Plot
# A scatter plot is a diagram where each value in the data set is represented by a dot.
# The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print("scatter plot:")
plt.scatter(x, y)
plt.show()
# The x-axis represents ages, and the y-axis represents speeds.

# Let us create two arrays that are both filled with 1000 random numbers from a normal data distribution.

# The first array will have the mean set to 5.0 with a standard deviation of 1.0.

# The second array will have the mean set to 10.0 with a standard deviation of 2.0:
# with bigger data sets
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)
print("scatter plot: with big data sets")
plt.scatter(x, y)
plt.show()
# We can see that the dots are concentrated around the value 5 on the x-axis, and 10 on the y-axis.

# We can also see that the spread is wider on the y-axis than on the x-axis.

# Linear Regression
# Linear regression uses the relationship between the data-points to draw a straight line through all them.

# This line can be used to predict future values.


import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Execute a method that returns some important key values of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Create a function that uses the slope and intercept values to return a new value. This new value represents where on the y-axis the corresponding x value will be placed:
def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

print("Creating linear regression model:")
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


# Polynomial Regression
# If your data points clearly will not fit a linear regression (a straight line through all data points), it might be ideal for polynomial regression.

# Polynomial regression, like linear regression, uses the relationship between the variables x and y to find the best way to draw a line through the data points.
import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)
print("Creating polynomial regression model:")
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# R-Squared

# It is important to know how well the relationship between the values of the x- and y-axis is, if there are no relationship the polynomial regression can not be used to predict anything.

# The relationship is measured with a value called the r-squared.

# The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.

import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
print("R-squared value:")
print(r2_score(y, mymodel(x)))


# Predict Future Values
# Now we can use the information we have gathered to predict future values.
#
# Example: Let us try to predict the speed of a car that passes the tollbooth at around the time 17:00:

# To do so, we need the same mymodel array from the example above:

import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
print("Predict speed of the car passing at 17:00: ")
speed = mymodel(17)
print(speed)


# Bad fit for Polynomial regression
import numpy
import matplotlib.pyplot as plt

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# bad releationship score check for Polynomial regression
import numpy
from sklearn.metrics import r2_score

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
print("R-squared value for bad fit check:")
print(r2_score(y, mymodel(x)))

# The result: 0.00995 indicates a very bad relationship, and tells us that this data set is not suitable for polynomial regression.



# Multiple Regression

import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])
print("Predicted CO2 emission:")
print(predictedCO2)
# We have predicted that a car with 1.3 liter engine, and a weight of 2300 kg, will release approximately 107 grams of CO2 for every kilometer it drives.

# Coefficient
# The coefficient is a factor that describes the relationship with an unknown variable.

# Example: if x is a variable, then 2x is x two times. x is the unknown variable, and the number 2 is the coefficient.

# In this case, we can ask for the coefficient value of weight against CO2, and for volume against CO2. The answer(s) we get tells us what would happen if we increase, or decrease, one of the independent values.

import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)

# [0.00755095 0.00780526]
"""The result array represents the coefficient values of weight and volume.

Weight: 0.00755095
Volume: 0.00780526

These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.

And if the engine size (Volume) increases by 1cm3, the CO2 emission increases by 0.00780526g.

I think that is a fair guess, but let test it!

We have already predicted that if a car with a 1300cm3 engine weighs 2300kg, the CO2 emission will be approximately 107g."""
