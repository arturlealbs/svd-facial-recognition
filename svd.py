import numpy as np

def svd(A):
    return _U(A), _S(A), _V(A)

def _U( M): 
    B = np.dot(M, M.T) 
    eigenvalues, eigenvectors = np.linalg.eig(B) 
    ncols = np.argsort(eigenvalues)[::-1] 

    return eigenvectors[:,ncols] 

def _V( M): 
    B = np.dot(M.T, M)
    eigenvalues, eigenvectors = np.linalg.eig(B) 
    ncols = np.argsort(eigenvalues)[::-1] 

    return eigenvectors[:,ncols].T 

def _S( M): 
    if (np.size(np.dot(M, M.T)) > np.size(np.dot(M.T, M))): 
        newM = np.dot(M.T, M) 
    else: 
        newM = np.dot(M, M.T) 
        
    eigenvalues, eigenvectors = np.linalg.eig(newM) 
    eigenvalues = np.sqrt(eigenvalues) 
    return eigenvalues[::-1] 
    