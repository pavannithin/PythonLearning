import pandas as pd;

mixedArray = pd.array([1, 2, '3'])

print(mixedArray)

# Time stamp
timestamp = pd.Timestamp('2026-01-30', tz='US/Central')
print(timestamp)

print(timestamp.year)
print(timestamp.month)
print(timestamp.day)

timedelta = pd.Timedelta('1 days')
print(timedelta)
print(timedelta.components)

# interval
iv = pd.Interval(left=0, right=10)

print(iv)
print(11 in iv)

ts1 = pd.Timestamp('2020-01-01 01:00:00')
ts2 = pd.Timestamp('2020-01-03 00:00:00')

print(ts2 - ts1)
print(ts2 > ts1)
print(ts2 < ts1)
print(ts2 == ts1)

mySeries = pd.Series([1, 2, 2, 1, 3, 4])
print(mySeries)

categorical = pd.Categorical(mySeries)

print(type(categorical))


df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
print(df)

timeDiff = df.between_time(ts1, ts2)

print(timeDiff)
