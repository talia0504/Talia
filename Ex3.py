# Name: Talia amsalem, Lior ohana
# ID: 207074691, 206101891
import numpy as np


def gauss_zeidel(matrix, vector, tolerence, max_iterations):
    print("Original equation system:")
    for i in range(matrix.shape[0]):
        row = ["{0:3g}*x{1}".format(matrix[i, j], j + 1) for j in range(matrix.shape[1])]
        print("{0} = {1:3g}".format(" + ".join(row), vector[i]))
    print("--------------------")

    x = np.zeros_like(vector)
    for it_count in range(1, max_iterations):
        x_new = np.zeros_like(x)
        print("Iteration {0}, current approximation: {1}".format(it_count, x))
        for i in range(matrix.shape[0]):
            s1 = np.dot(matrix[i, :i], x_new[:i])
            s2 = np.dot(matrix[i, i + 1:], x[i + 1:])
            x_new[i] = (vector[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=tolerence):
            break
        x = x_new
    print("--------------------")

    print("Final approximation:")
    print(x)
    print("--------------------")
    error = np.dot(matrix, x) - vector
    print("Final error:")
    print(error)


def jacobi(matrix, vector, tolerence, max_iterations):
    print("Original equation system:")
    for i in range(matrix.shape[0]):
        row = ["{}*x{}".format(matrix[i, j], j + 1) for j in range(matrix.shape[1])]
        print(" + ".join(row), "=", vector[i])
    print("-------------------------")

    iterations = 1
    x = np.zeros_like(vector)
    for it_count in range(max_iterations):
        print("Iteration {}".format(iterations) + ", Current approximation:", x)
        x_new = np.zeros_like(x)

        for i in range(matrix.shape[0]):
            s1 = np.dot(matrix[i, :i], x[:i])
            s2 = np.dot(matrix[i, i + 1:], x[i + 1:])
            x_new[i] = (vector[i] - s1 - s2) / matrix[i, i]

        if np.allclose(x, x_new, atol=tolerence, rtol=0.):
            break

        x = x_new
        iterations = iterations + 1

    print("-------------------------")
    print("Final approximation:")
    print(x)
    print("-------------------------")
    error = np.dot(matrix, x) - b
    print("Final error:")
    print(error)


def Dominant_diagonal(A):
    if abs(A[0][0] > A[0][1] + A[0][2]) and abs(A[1][1] > A[1][0] + A[1][2]) and abs(A[2][2] > A[2][0] + A[2][1]):
        print("Is Dominant_diagonal")
        return True
    print("Not Dominant_diagonal")
    return False


A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])

b = np.array([6., 25., -11., 15.])

jacobi(A, b, 0.001, 20)
gauss_zeidel(A, b, 0.001, 20)
Dominant_diagonal(A)
