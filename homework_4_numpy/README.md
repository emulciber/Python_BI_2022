# Functions for numpy array operations

File numpy_challenge.py contains some functions to operate with numpy arrays and matrices.

You need __numpy__ library to use this functions.   
For example you may import this file as module with `import numpy_challenge as npc` and use functions like `npc.matrix_multiplication(matrix1, matrix2)`.

* `matrix_multiplication` takes two matrices and multiply them.
* `multiplication_check` takes list of matrices and checks the possibility of successive multiplication.
* `multiply_matrices` takes list of matrices and multiplies them sequentially.
* `compute_2d_distance` takes two arrays (with 2 numbers in array) and computes distance between them.
* `compute_multidimensional_distance` takes two arrays and computes distance between them.
* `compute_pair_distances` takes array with some rows and returns matrix with pair distances between each two rows.

Tested with:   
python==3.8.8   
numpy==1.23.4