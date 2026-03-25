import time
import numpy as np

# Number of elements
n = 1_000_000

# Create Python list
python_list = list(range(n))

# Create NumPy array
numpy_array = np.arange(n)

# ----- Python List Speed Test -----
start_time = time.time()
list_result = [x + 5 for x in python_list]
list_time = time.time() - start_time

# ----- NumPy Array Speed Test -----
start_time = time.time()
numpy_result = numpy_array + 5
numpy_time = time.time() - start_time

# Print results
print("Python List Execution Time:", list_time, "seconds")
print("NumPy Array Execution Time:", numpy_time, "seconds")