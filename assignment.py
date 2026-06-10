import numpy as np
import pandas as pd

# 1. Create a NumPy array 'arr' of integers from 0 to 5 and print its data type.
arr = np.arange(6)
print(arr.dtype)

# 2. Given a NumPy array 'arr', check if its data type is float64.
def is_float64(arr):
    return arr.dtype == np.float64
# Example: print(is_float64(np.array([1.0, 2.0])))  # True

# 3. Create a NumPy array 'arr' with a data type of complex128 containing three complex numbers.
arr = np.array([1+2j, 3+4j, 5+6j], dtype=np.complex128)

# 4. Convert an existing NumPy array 'arr' of integers to float32 data type.
arr_int = np.array([1, 2, 3])
arr_float32 = arr_int.astype(np.float32)

# 5. Given a NumPy array 'arr' with float64 data type, convert it to float32 to reduce decimal precision.
arr_float64 = np.array([1.123456789, 2.987654321])
arr_float32 = arr_float64.astype(np.float32)

# 6. Write a function array_attributes that takes a NumPy array as input and returns its shape, size, and data type.
def array_attributes(arr):
    return arr.shape, arr.size, arr.dtype

# 7. Create a function array_dimension that takes a NumPy array as input and returns its dimensionality.
def array_dimension(arr):
    return arr.ndim

# 8. Design a function item_size_info that takes a NumPy array as input and returns the item size and the total size in bytes.
def item_size_info(arr):
    return arr.itemsize, arr.nbytes

# 9. Create a function array_strides that takes a NumPy array as input and returns the strides of the array.
def array_strides(arr):
    return arr.strides

# 10. Design a function shape_stride_relationship that takes a NumPy array as input and returns the shape and strides of the array.
def shape_stride_relationship(arr):
    return arr.shape, arr.strides

# 11. Create a function `create_zeros_array` that takes an integer `n` as input and returns a NumPy array of zeros with `n` elements.
def create_zeros_array(n):
    return np.zeros(n)

# 12. Write a function `create_ones_matrix` that takes integers `rows` and `cols` as inputs and generates a 2D NumPy array filled with ones of size `rows x cols`.
def create_ones_matrix(rows, cols):
    return np.ones((rows, cols))

# 13. Write a function `generate_range_array` that takes three integers start, stop, and step as arguments and creates a NumPy array with a range starting from `start`, ending at stop (exclusive), and with the specified `step`.
def generate_range_array(start, stop, step):
    return np.arange(start, stop, step)

# 14. Design a function `generate_linear_space` that takes two floats `start`, `stop`, and an integer `num` as arguments and generates a NumPy array with num equally spaced values between `start` and `stop` (inclusive).
def generate_linear_space(start, stop, num):
    return np.linspace(start, stop, num)

# 15. Create a function `create_identity_matrix` that takes an integer `n` as input and generates a square identity matrix of size `n x n` using `numpy.eye`.
def create_identity_matrix(n):
    return np.eye(n)

# 16. Write a function that takes a Python list and converts it into a NumPy array.
def list_to_numpy(lst):
    return np.array(lst)

# 17. Create a NumPy array and demonstrate the use of `numpy.view` to create a new array object with the same data.
arr = np.array([1, 2, 3])
view_arr = arr.view()
view_arr[0] = 99
print(arr)  # [99 2 3] -> original changed because view shares data

# 18. Write a function that takes two NumPy arrays and concatenates them along a specified axis.
def concatenate_arrays(arr1, arr2, axis=0):
    return np.concatenate((arr1, arr2), axis=axis)

# 19. Create two NumPy arrays with different shapes and concatenate them horizontally using `numpy.concatenate`.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6, 7], [8, 9, 10]])
c = np.concatenate((a, b), axis=1)  # horizontal concat (same number of rows)

# 20. Write a function that vertically stacks multiple NumPy arrays given as a list.
def vertical_stack(arrays):
    return np.vstack(arrays)

# 21. Write a Python function using NumPy to create an array of integers within a specified range (inclusive) with a given step size.
def inclusive_range(start, stop, step):
    return np.arange(start, stop + step, step)

# 22. Write a Python function using NumPy to generate an array of 10 equally spaced values between 0 and 1 (inclusive).
arr = np.linspace(0, 1, 10)

# 23. Write a Python function using NumPy to create an array of 5 logarithmically spaced values between 1 and 1000 (inclusive).
arr = np.logspace(0, 3, 5)  # 10^0 = 1, 10^3 = 1000

# 24. Create a Pandas DataFrame using a NumPy array that contains 5 rows and 3 columns, where the values are random integers between 1 and 100.
np.random.seed(42)
data = np.random.randint(1, 101, size=(5, 3))
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# 25. Write a function that takes a Pandas DataFrame and replaces all negative values in a specific column with zeros. Use NumPy operations within the Pandas DataFrame.
def replace_negatives(df, column):
    df[column] = np.where(df[column] < 0, 0, df[column])
    return df

# 26. Access the 3rd element from the given NumPy array. arr = np.array([10, 20, 30, 40, 50])
arr = np.array([10, 20, 30, 40, 50])
print(arr[2])  # 30

# 27. Retrieve the element at index (1, 2) from the 2D NumPy array. arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[1, 2])  # 6

# 28. Using boolean indexing, extract elements greater than 5 from the given NumPy array. arr = np.array([3,8,2,10,5,7])
arr = np.array([3, 8, 2, 10, 5, 7])
print(arr[arr > 5])  # [ 8 10  7]

# 29. Perform basic slicing to extract elements from index 2 to 5 (inclusive) from the given NumPy array. arr = np.array([1,2,3,4,5,6,7,8,9])
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[2:6])  # [3 4 5 6]

# 30. Slice the 2D NumPy array to extract the sub-array `[[2, 3], [5, 6]]` from the given array. arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sub = arr_2d[:2, 1:3]  # [[2 3] [5 6]]
print(sub)

# 31. Write a NumPy function to extract elements in specific order from a given 2D array based on indices provided in another array.
def extract_by_indices(arr_2d, indices):
    # indices is a list of [row_indices, col_indices]
    return arr_2d[indices[0], indices[1]]
# Example: arr = np.arange(12).reshape(3,4); idx = [[0,1,2],[1,2,3]] -> arr[idx[0], idx[1]]

# 32. Create a NumPy function that filters elements greater than a threshold from a given 1D array using boolean indexing.
def filter_above_threshold(arr, threshold):
    return arr[arr > threshold]

# 33. Develop a NumPy function that extracts specific elements from a 3D array using indices provided in three separate arrays for each dimension.
def extract_3d_indices(arr_3d, i_arr, j_arr, k_arr):
    return arr_3d[i_arr, j_arr, k_arr]

# 34. Write a NumPy function that returns elements from an array where both two conditions are satisfied using boolean indexing.
def both_conditions(arr, cond1, cond2):
    return arr[(cond1) & (cond2)]

# 35. Create a NumPy function that extracts elements from a 2D array using row and column indices provided in separate arrays.
def extract_rows_cols(arr_2d, rows, cols):
    return arr_2d[rows, cols]

# 36. Given an array arr of shape (3, 3), add a scalar value of 5 to each element using NumPy broadcasting.
arr = np.ones((3, 3))
result = arr + 5

# 37. Consider two arrays arr1 of shape (1, 3) and arr2 of shape (3, 4). Multiply each row of arr2 by the corresponding element in arr1 using NumPy broadcasting.
arr1 = np.array([2, 3, 4]).reshape(3, 1)  # reshape to (3,1) for proper broadcasting
arr2 = np.ones((3, 4))
result = arr2 * arr1  # each row of arr2 multiplied by corresponding scalar from arr1

# 38. Given a 1D array arr1 of shape (1, 4) and a 2D array arr2 of shape (4, 3), add arr1 to each row of arr2 using NumPy broadcasting.
# To add arr1 to each row of arr2, arr1 must be reshaped to (1,4) and arr2 to (4,4) or arr1 to (4,1)? Actually shape mismatch: (1,4) and (4,3) cannot broadcast. Assuming intended arr2.shape (4,4).
arr1 = np.array([1, 2, 3, 4]).reshape(1, 4)
arr2 = np.ones((4, 4))
result = arr1 + arr2

# 39. Consider two arrays arr1 of shape (3, 1) and arr2 of shape (1, 3). Add these arrays using NumPy broadcasting.
arr1 = np.array([1, 2, 3]).reshape(3, 1)
arr2 = np.array([4, 5, 6]).reshape(1, 3)
result = arr1 + arr2  # produces (3,3) matrix

# 40. Given arrays arr1 of shape (2, 3) and arr2 of shape (2, 2), perform multiplication using NumPy broadcasting. Handle the shape incompatibility.
arr1 = np.ones((2, 3))
arr2 = np.ones((2, 2))
# Incompatible: cannot broadcast (2,3) and (2,2). One fix: pad arr2 to (2,3) by repeating last column.
arr2_padded = np.hstack((arr2, np.ones((2, 1))))
result = arr1 * arr2_padded

# 41. Calculate column wise mean for the given array: arr = np.array([[1,2,3],[4,5,6]])
arr = np.array([[1, 2, 3], [4, 5, 6]])
col_mean = np.mean(arr, axis=0)

# 42. Find maximum value in each row of the given array: arr = np.array([[1,2,3],[4,5,6]])
row_max = np.max(arr, axis=1)

# 43. For the given array, find indices of maximum value in each column: arr = np.array([[1,2,3],[4,5,6]])
col_argmax = np.argmax(arr, axis=0)

# 44. For the given array, apply custom function to calculate moving sum along rows: arr = np.array([[1,2,3],[4,5,6]])
def moving_sum_rows(arr, window):
    return np.apply_along_axis(lambda row: np.convolve(row, np.ones(window, dtype=int), mode='valid'), axis=1, arr=arr)
result = moving_sum_rows(arr, 2)  # example window=2

# 45. In the given array, check if all elements in each column are even: arr = np.array([[2,4,6],[3,5,7]])
arr = np.array([[2, 4, 6], [3, 5, 7]])
col_all_even = np.all(arr % 2 == 0, axis=0)

# 46. Given a NumPy array arr, reshape it into a matrix of dimensions `m` rows and `n` columns. Return the reshaped matrix.
def reshape_matrix(arr, m, n):
    return arr.reshape(m, n)

# 47. Create a function that takes a matrix as input and returns the flattened array.
def flatten_matrix(mat):
    return mat.flatten()

# 48. Write a function that concatenates two given arrays along a specified axis.
def concat_along_axis(arr1, arr2, axis=0):
    return np.concatenate((arr1, arr2), axis=axis)

# 49. Create a function that splits an array into multiple sub-arrays along a specified axis.
def split_array(arr, indices_or_sections, axis=0):
    return np.split(arr, indices_or_sections, axis=axis)

# 50. Write a function that inserts and then deletes elements from a given array at specified indices.
def insert_then_delete(arr, insert_indices, values, delete_indices):
    new_arr = np.insert(arr, insert_indices, values)
    new_arr = np.delete(new_arr, delete_indices)
    return new_arr

# 51. Create a NumPy array `arr1` with random integers and another array `arr2` with integers from 1 to 10. Perform element-wise addition.
np.random.seed(0)
arr1 = np.random.randint(0, 10, size=10)
arr2 = np.arange(1, 11)
result = arr1 + arr2

# 52. Generate a NumPy array `arr1` with sequential integers from 10 to 1 and another array `arr2` with integers from 1 to 10. Subtract `arr2` from `arr1` element-wise.
arr1 = np.arange(10, 0, -1)
arr2 = np.arange(1, 11)
result = arr1 - arr2

# 53. Create a NumPy array `arr1` with random integers and another array `arr2` with integers from 1 to 5. Perform element-wise multiplication.
arr1 = np.random.randint(1, 10, size=5)
arr2 = np.arange(1, 6)
result = arr1 * arr2

# 54. Generate a NumPy array `arr1` with even integers from 2 to 10 and another array `arr2` with integers from 1 to 5. Perform element-wise division of `arr1` by `arr2`.
arr1 = np.arange(2, 11, 2)
arr2 = np.arange(1, 6)
result = arr1 / arr2

# 55. Create a NumPy array `arr1` with integers from 1 to 5 and another array `arr2` with the same numbers reversed. Calculate the exponentiation of `arr1` raised to the power of `arr2` element-wise.
arr1 = np.arange(1, 6)
arr2 = np.arange(5, 0, -1)
result = arr1 ** arr2

# 56. Write a function that counts the occurrences of a specific substring within a NumPy array of strings. arr = np.array(['hello', 'world', 'hello', 'numpy', 'hello'])
def count_substring(arr, sub):
    return np.char.count(arr, sub).sum()
arr = np.array(['hello', 'world', 'hello', 'numpy', 'hello'])
print(count_substring(arr, 'ell'))  # 3

# 57. Write a function that extracts uppercase characters from a NumPy array of strings. arr = np.array(['Hello', 'World', 'OpenAI', 'GPT'])
def extract_uppercase(arr):
    return [''.join([c for c in s if c.isupper()]) for s in arr]
arr = np.array(['Hello', 'World', 'OpenAI', 'GPT'])
print(extract_uppercase(arr))

# 58. Write a function that replaces occurrences of a substring in a NumPy array of strings with a new string. arr = np.array(['apple', 'banana', 'grape', 'pineapple'])
def replace_substring(arr, old, new):
    return np.char.replace(arr, old, new)
arr = np.array(['apple', 'banana', 'grape', 'pineapple'])
print(replace_substring(arr, 'ap', 'XX'))

# 59. Write a function that concatenates strings in a NumPy array element-wise. arr1 = np.array(['Hello', 'World']); arr2 = np.array(['Open', 'AI'])
def concat_strings(arr1, arr2):
    return np.char.add(arr1, arr2)
arr1 = np.array(['Hello', 'World'])
arr2 = np.array(['Open', 'AI'])
print(concat_strings(arr1, arr2))

# 60. Write a function that finds the length of the longest string in a NumPy array. arr = np.array(['apple', 'banana', 'grape', 'pineapple'])
def longest_string_length(arr):
    return np.char.str_len(arr).max()
arr = np.array(['apple', 'banana', 'grape', 'pineapple'])
print(longest_string_length(arr))

# 61. Create a dataset of 100 random integers between 1 and 1000. Compute mean, median, variance, standard deviation.
data = np.random.randint(1, 1001, size=100)
mean = np.mean(data)
median = np.median(data)
variance = np.var(data)
std = np.std(data)

# 62. Generate an array of 50 random numbers between 1 and 100. Find the 25th and 75th percentiles.
data = np.random.randint(1, 101, size=50)
p25 = np.percentile(data, 25)
p75 = np.percentile(data, 75)

# 63. Create two arrays representing two sets of variables. Compute the correlation coefficient using NumPy's `corrcoef`.
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5
corr = np.corrcoef(x, y)

# 64. Create two matrices and perform matrix multiplication using NumPy's `dot` function.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)  # or A @ B

# 65. Create an array of 50 integers between 10 and 1000. Calculate 10th, 50th (median), 90th percentiles and first/third quartiles.
data = np.random.randint(10, 1001, size=50)
p10 = np.percentile(data, 10)
p50 = np.percentile(data, 50)
p90 = np.percentile(data, 90)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

# 66. Create a NumPy array of integers and find the index of a specific element. arr = np.array([12, 25, 6, 42, 8, 30])
arr = np.array([12, 25, 6, 42, 8, 30])
index = np.where(arr == 42)[0][0]  # returns first occurrence
print(index)

# 67. Generate a random NumPy array and sort it in ascending order.
np.random.seed(0)
arr = np.random.randint(0, 50, size=10)
sorted_arr = np.sort(arr)

# 68. Filter elements >20 in the given NumPy array. arr = np.array([10, 20, 30, 40, 50])
arr = np.array([10, 20, 30, 40, 50])
result = arr[arr > 20]

# 69. Filter elements which are divisible by 3 from a given NumPy array. arr = np.array([1, 5, 8, 12, 15])
arr = np.array([1, 5, 8, 12, 15])
result = arr[arr % 3 == 0]

# 70. Filter elements which are ≥ 20 and ≤ 40 from a given NumPy array. arr = np.array([10, 20, 30, 40, 50])
arr = np.array([10, 20, 30, 40, 50])
result = arr[(arr >= 20) & (arr <= 40)]

# 71. For the given NumPy array, check its byte order using the `dtype` attribute byteorder. arr = np.array([1, 2, 3])
arr = np.array([1, 2, 3])
print(arr.dtype.byteorder)  # '=' for native

# 72. For the given NumPy array, perform byte swapping in place using `byteswap()`. arr = np.array([1, 2, 3])
arr = np.array([1, 2, 3], dtype=np.int32)
arr.byteswap(inplace=True)

# 73. For the given NumPy array, swap its byte order without modifying the original array.
arr = np.array([1, 2, 3], dtype=np.int32)
new_arr = arr.byteswap().view(arr.dtype.newbyteorder())  # original unchanged

# 74. For the given NumPy array, swap its byte order conditionally based on system endianness.
def conditional_byteswap(arr):
    if arr.dtype.byteorder != '=':
        return arr.byteswap().view(arr.dtype.newbyteorder())
    return arr

# 75. For the given NumPy array, check if byte swapping is necessary for the current system using `dtype` attribute `byteorder`.
def swapping_needed(arr):
    return arr.dtype.byteorder != '='

# 76. Create a NumPy array `arr1` with values from 1 to 10. Create a copy `copy_arr` and modify an element. Check if modifying `copy_arr` affects `arr1`.
arr1 = np.arange(1, 11)
copy_arr = arr1.copy()
copy_arr[0] = 100
print(arr1[0])  # 1, unchanged

# 77. Create a 2D NumPy array `matrix` of shape (3,3) with random integers. Extract a slice `view_slice` and modify an element. Observe if original changes.
matrix = np.random.randint(0, 10, (3, 3))
view_slice = matrix[1:3, 1:3]
view_slice[0, 0] = 999
print(matrix)  # original changed because slice is a view

# 78. Create a NumPy array `array_a` of shape (4,3) with sequential integers 1..12. Extract a slice `view_b` and broadcast addition of 5. Check if original changes.
array_a = np.arange(1, 13).reshape(4, 3)
view_b = array_a[1:3, :]  # slice view
view_b += 5
print(array_a)  # original changed

# 79. Create a NumPy array `orig_array` of shape (2,4) with values 1..8. Create a reshaped view `reshaped_view` of shape (4,2). Modify an element and check original.
orig_array = np.arange(1, 9).reshape(2, 4)
reshaped_view = orig_array.reshape(4, 2)
reshaped_view[0, 0] = 99
print(orig_array)  # original changed (first element becomes 99)

# 80. Create a NumPy array `data` of shape (3,4) with random integers. Extract a copy `data_copy` of elements >5. Modify an element in copy and verify original unchanged.
data = np.random.randint(0, 10, (3, 4))
data_copy = data[data > 5].copy()
if data_copy.size > 0:
    data_copy[0] = 1000
print(data)  # original unchanged

# 81. Create two matrices A and B of identical shape containing integers and perform addition and subtraction.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
add = A + B
sub = A - B

# 82. Generate two matrices `C` (3x2) and `D` (2x4) and perform matrix multiplication.
C = np.random.randint(1, 5, (3, 2))
D = np.random.randint(1, 5, (2, 4))
prod = np.dot(C, D)  # or C @ D

# 83. Create a matrix `E` and find its transpose.
E = np.array([[1, 2, 3], [4, 5, 6]])
transpose = E.T

# 84. Generate a square matrix `F` and compute its determinant.
F = np.array([[1, 2], [3, 4]])
det = np.linalg.det(F)

# 85. Create a square matrix `G` and find its inverse.
G = np.array([[4, 7], [2, 6]])
inv = np.linalg.inv(G)