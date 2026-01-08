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