"""
Import libraries
"""
import numpy as np
import sys
import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

"""
Auxiliary functions
"""

class corr_matrix:
    
    def __init__(self, n_processes, min_rho, max_rho):
        self.n_processes = n_processes
        self.min_rho = min_rho
        self.max_rho = max_rho
        
    def create_corrmat(self):
        
        # Create the Pearson correlation coefficient matrix
        rho = np.random.uniform(self.min_rho,self.max_rho,(self.n_processes,self.n_processes))
        np.fill_diagonal(rho,1)
        pearson_matrix = (rho + rho.T)/2
        return pearson_matrix
    
class cholesky_decomposition:
    
    def __init__(self, A):
        self.A = A

    def check_symmetry(self):
        
        if ((self.A.transpose() == self.A).all()):
            print("The input matrix is symmetric!")
        else:
            print("The input matrix is not symmetric! We will transform it into a symmetric one!")
            self.A = np.dot(self.A.transpose(),self.A)
    
    def check_positive_definite(self):
        if((np.linalg.eigvals(self.A) > 0).all()):
            print("The input matrix is positive definite!")
        else:
            sys.exit("The input matrix is not positive definite! the program is now closing.")

    def cholesky_algorithm(self):
        L = np.zeros(self.A.shape)
        for row in range(0, self.A.shape[0], 1):
            for col in range(0, self.A.shape[1], 1):
                
                tmp_sum = sum([L[row, j]*L[col, j] for j in range(0,col,1)])
                
                if (col == row):
                    L[row,col] = math.sqrt(self.A[row,col] - tmp_sum)
                elif (row > col):
                    L[row,col] = (1.0/float(L[col,col]))*(self.A[row,col] - tmp_sum)
                else:
                    pass
        
        return L, L.transpose()

class analyze_processes:
    
    def __init__(self,X):
        self.X = X
    
    def pairplot(self):
        names =  ['time series #' + str(i) for i in range(1,self.X.shape[0] + 1,1)]
        plt.figure()
        sns.pairplot(pd.DataFrame(np.diff(self.X).T, columns=names))
    
    def corr_map(self):
        names =  ['time series #' + str(i) for i in range(1,self.X.shape[0] + 1,1)]
        corr_mat = pd.DataFrame(np.diff(self.X).T, columns=names).corr()
        plt.figure()
        sns.heatmap(corr_mat, annot=True)
        
    
    
class data_generating_process:
    
    def __init__(self,n_processes,T,dt,mu,sd,p0,min_rho,max_rho,produce_analysis):
        
        self.n_processes = n_processes
        self.T = T
        self.dt = dt
        self.mu = mu
        self.sd = sd
        self.p0 = p0
        self.min_rho = min_rho
        self.max_rho = max_rho
        self.produce_analysis = produce_analysis
    
    
    def gbm_euler_simulator(self):
        
        corr_mat_object = corr_matrix(self.n_processes,self.min_rho,self.max_rho)
        R = corr_mat_object.create_corrmat()
        
        chol_object = cholesky_decomposition(R)
        chol_object.check_symmetry()
        chol_object.check_positive_definite()
        L, U = chol_object.cholesky_algorithm()
        
        N = int(self.T/self.dt)
        P = np.zeros((L.shape[0], self.T))
        P[:,0] = self.p0
        for i in range(1,N):
            p = self.p0*np.exp((self.mu - 0.5*(self.sd**2))*self.dt + self.sd*np.sqrt(self.dt)*np.dot(L,np.random.normal(0,1,L.shape[0])))
            if ((i*self.dt)%1 == 0):
                P[:,int(i*self.dt)] = p
        
        if self.produce_analysis:
            plot_object = analyze_processes(P)
            plot_object.pairplot()
            plot_object.corr_map()
        return P


n_processes = 4

mu = np.zeros(n_processes)
sd = np.random.uniform(0.0,0.2,n_processes)
p0 = 100
T = 252*5
dt = 1/252
min_rho = -1
max_rho = 1
produce_analysis = True

process_object = data_generating_process(n_processes,T,dt,mu,sd,p0,min_rho,max_rho,produce_analysis)
X = process_object.gbm_euler_simulator()