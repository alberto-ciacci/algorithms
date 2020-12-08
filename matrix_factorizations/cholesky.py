import numpy as np
import math
import pprint
import sys

def check_symmetry():
    global A
    if ((A.transpose() == A).all()):
        print("The input matrix is symmetric!")
    else:
        print("The input matrix is not symmetric! We will transform it into a symmetric one!")
        A = symmetrize_matrix(A)

def symmetrize_matrix(A):
    return np.dot(A.transpose(),A)
    

def check_positive_definite():
    if((np.linalg.eigvals(A) > 0).all()):
        print("The input matrix is positive definite!")
    else:
        sys.exit("The input matrix is not positive definite! the program is now closing.")

def cholesky_algorithm():
    L = np.zeros(A.shape)
    for row in range(0, A.shape[0], 1):
        for col in range(0, A.shape[1], 1):
            
            tmp_sum = sum([L[row, j]*L[col, j] for j in range(0,col,1)])
            
            if (col == row):
                L[row,col] = math.sqrt(A[row,col] - tmp_sum)
            elif (row > col):
                L[row,col] = (1.0/float(L[col,col]))*(A[row,col] - tmp_sum)
            else:
                pass
    
    return L, L.transpose()

def cholesky_determinant():
    L_det = L.diagonal().prod()
    return L_det**2


if __name__ == "__main__":
    
    # The user should specify a matrix here
    A = np.array([[2, 7, 4, 5], [2, 4, 5, 2], [6, 8, 10, 7], [6, 3, 8, 2]])
    # Check if the matrix is symmetric
    check_symmetry()
    # Check if the matrix is positive definite
    check_positive_definite()
    # Perform Cholesky Decomposition
    L, U = cholesky_algorithm()
    # Print the output
    print('Original matrix A (eventually symmetrized): ')
    pprint.pprint(A)
    print('Decomposed lower triangular matrix L: ')
    pprint.pprint(L)
    print('Decomposed upper triangular matrix U: ')
    pprint.pprint(U)
    # Exploit the Cholesky Decomposition to calculate the determinant of the input matrix
    print('We exploit the Cholesky Decomposition to calculate the determinant of A: ')
    print('Det(A) = Det(LU) = Det(L)*Det(U) = Det(L)^2: {:8.3f}'.format(cholesky_determinant()))
    
    