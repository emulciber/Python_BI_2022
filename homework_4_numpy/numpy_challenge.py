import numpy as np


def matrix_multiplication(matrix_1, matrix_2):
    return matrix_1 @ matrix_2


def multiplication_check(matrix_list):
    last_matrix_shape = matrix_list[0].shape[1]
    for i in range(1, len(matrix_list)):
        if last_matrix_shape != matrix_list[i].shape[0]:
            return False
        last_matrix_shape = matrix_list[i].shape[1]
    return True


def multiply_matrices(matrix_list):
    try:
        last_matrix = matrix_list[0]
        for i in range(1, len(matrix_list)):
            last_matrix = last_matrix @ matrix_list[i]
        return last_matrix
    except:
        return None


def compute_2d_distance(arr1, arr2):
    return np.sqrt(np.sum((arr2 - arr1) ** 2))


def compute_multidimensional_distance(arr1, arr2):
    return np.sqrt(np.sum((arr2 - arr1) ** 2))


def compute_pair_distances(arr):
    #return np.sqrt(np.sum((arr[:, None, :] - arr[None, :, :]) ** 2, axis=-1))
    return np.linalg.norm(arr[:, None, :] - arr[None, :, :], axis=-1)


if __name__== '__main__':

    np.array([[1,2,3], [4,5,6], [7,8,9]])
    np.linspace(0, 3, 9)
    np.arange(1, 9.5, 0.5)


    # Test arrays and functions

    # matrix_1 = np.array([[1,3], [2,4], [5,8]])
    # matrix_2 = np.array([[1,4,6,7], [2,2,4,1]])
    # print(matrix_multiplication(matrix_1, matrix_2))

    # matrix_list_true = [matrix_1, matrix_2, np.array([[1,3,5], [2,1,1], [3,4,7], [1,8,1]]), np.array([[2,2], [1,2], [2,2]])]
    # matrix_list_false = [matrix_1, matrix_2, np.array([[1,3,5], [2,1,1], [3,4,7]]), np.array([[2,2], [1,2], [2,2]])]
    # print(multiplication_check(matrix_list_false))
    # print(multiply_matrices(matrix_list_false))

    # arr1 = np.array([37,44])
    # arr2 = np.array([5,16])
    # print(compute_2d_distance(arr1, arr2))
    # print(compute_multidimensional_distance(arr1, arr2))

    # arr = np.array([[37, 44, 5], [11, 8, 13], [1,4,7], [2,2,5]])
    # arr = np.array([[0,0],[1,1],[2,2]])
    # print(compute_pair_distances(arr))