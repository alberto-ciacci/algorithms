import numpy as np
import pprint
import sys
import matplotlib.pyplot as plt

def check_diagonalizable():
    # Eigendecomposition requires the input to be diagonalizable -> Eigenmatrix must be full rank
    D, P = np.linalg.eig(A)    
    rank_P = np.linalg.matrix_rank(P)
    if (rank_P == np.min(P.shape)):
        print("The input matrix is diagonalizable!")
        return np.diag(D), P
    else:
        sys.exit("The input matrix is not diagonalizable! the program is now closing.")

def eigendecomposition():
    # Recall that for orthogonal matrices (i.e., columns are linearly independent and normalized) A^T = A^{-1}
    return np.linalg.multi_dot([P,D,P.transpose()])

def eigen_determinant():
    return np.prod(np.diagonal(D))

def plot_vectors():
    n_rows = M.shape[0]
    n_cols = M.shape[1]
    if (n_rows == 2):
        largest = np.maximum(0,np.max(M[:])) + 0.1
        lowest  = np.minimum(0,np.min(M[:])) - 0.1
        colors  = ['r','b']
        for i in range(n_cols):
            ax.arrow(0,0,M[0,i],M[1,i],
                     color = colors[i],
                     width = 0.01,
                     length_includes_head = True)
        ax.set_xlim(lowest, largest)
        ax.set_ylim(lowest, largest)
        ax.set_xlabel('First dimension')
        ax.set_ylabel('Second dimension')
        ax.set_title(title)

if __name__ == "__main__":
    
    # The user should specify a matrix here
    A = np.array([[2,1],[1,2]])
    # Check if the matrix is symmetric
    D, P = check_diagonalizable()
    # Perform the eigen-decomposition
    EA = eigendecomposition()
    # Print the output
    print('Eigenvector matrix P: ')
    pprint.pprint(P)
    print('Eigenvalues diagonal matrix D: ')
    pprint.pprint(D)
    print('Inverse eigenvector matrix P^{-1}: ')
    pprint.pprint(np.linalg.inv(P))
    # Exploit the eigendecomposition to calculate the determinant of the input matrix
    print('We exploit the Eigendecomposition to calculate the determinant of A: ')
    print('Det(A) = Det(PDP^-1) = Det(PDP^T) = Det(P)*Det(D)*Det(P^T) = Det(D): {:8.3f}'.format(eigen_determinant()))
    # Plot a step-by-step transformation of the eigenmatrix via eigen-decomposition
    fig, axes = plt.subplots(2,2, figsize= (10,10))
    titles = [r'$P^{T}P$ (basis change)',
              r'$AP$ (original transformation)',
              r'$DP^{T}P$ (stretching via eigenvalues)',
              r'$PDP^{T}P$ (return to original coordinates)']
    inputs = [np.dot(P.transpose(),P),
              np.dot(A, P),
              np.linalg.multi_dot([D, P.transpose(),P]),
              np.linalg.multi_dot([P, D, P.transpose(),P])]
    for ax,title,M in zip(axes.ravel(),titles,inputs):
        plot_vectors()
    plt.show()

    