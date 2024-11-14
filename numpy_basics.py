import numpy as np

"""CREATING ARRAYS"""

array1 = np.array([2,3,4])
array2 = np.zeros([2,3])
array3 = np.ones([2,3])
array4 = np.linspace(0,10,5)

print(f"ONE SIMPLE ARRAY:\n{array1}\nONE WITH ZEROS\n{array2}\nALL WITH ONES:\n{array3}\n LINESPACE(START,STEP,STOP):\n{array4}\n")

"""ARRAY OPERATIONS"""
array5 = np.array([2,3,4])
array6 = np.array([5,6,7])

sum_array = array5+array6
mul_array = array5*array6
scalar_array = array6*2
print(sum_array,mul_array,scalar_array)

"""INDEXING AND SLICING"""
array7 = np.array ([[1,2,3],[4,5,6],[7,8,9]])

#Basic slicing
print ("element at [1,2]", array7[1,2])

#SLICING
print(array7[:1])

#BOOLEAN INDEXING 
print("ELEMENTS > 5:",array7[array7>5])

"""aggeragations and math operations"""

#aggerate operations 
print("SUM OF THE ARRAY",np.sum(array7))
print("MEAN OF THE ARRAY", np.mean(array7))
print("MAX OF THE ARRAY",np.max(array7))

#sum along columns (axis=0) and rows (axis=1)
print('COLUMN SUM',np.sum(array7,axis=1))
print('ROW SUM',np.sum(array7,axis=1))

"""LINEAR NUMBERS AND SOME RANDOM NUMBERS """
matrix_a = np.array([[1,2],[2,3]])
matrix_b = np.array([[4,5],[6,7]])
dot_product = np.dot(matrix_b,matrix_a)
print("THE DOT PRODUCT FOR BOTH OF THEM ARE",dot_product)

#let's work with some random numbers 
random_array = np.random.rand(2,3)
random_int_array = np.random.randint(2,3,(2,2))
print(f"for the ranodm array we have the output{random_array},and if we specifically want the integers\n {random_int_array}")