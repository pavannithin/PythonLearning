

array=[[23,45,43,23,45],[45,67,54,32,45],[89,90,87,65,44],[23,45,67,32,10]]
#display
print(array)

#get the first row
print("First row:")
print(array[0])

#get the third row
print("Second row:")
print(array[2])

#get the first row third element
print("First row third element:")
print(array[0][2])
# access elements using for loop
print("Access elements using for loop:")
for rows in array:
 for columns in rows:
   print(columns,end=" ")
   print()

# insert element in 2nd row

#insert the row at 5 th position
array.insert(2, [1,2,3,4,5])

#insert the row at 6 th position
array.insert(2, [1,2,3,4,5])

#insert the row at 7 th position
array.insert(2, [1,2,3,4,5])

#display
print(array)

# Updating the values into the two-dimensional array
print("Updating the values into the two-dimensional array:")
#update row values in the 3rd row
array[2]=[0,3,5,6,7]

#update row values in the 5th row
array[2]=[0,3,5,6,7]

#update the first row , third column
array[0][2]=100

#update the second row , third column
array[1][2]=400

#display
print(array)

# Deleting the values from two-dimensional array

#creare 2D array with 4 rows and 5 columns
array=[[23,45,43,23,45],[45,67,54,32,45],[89,90,87,65,44],[23,45,67,32,10]]

#delete row values in the 3rd row
del array[2]

#delete row values in the 2nd row
del array[1]

#display
print(array)
