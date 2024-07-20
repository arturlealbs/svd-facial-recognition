import numpy as np

def svd(A):
    m, n = A.shape
    print(m,n)

    AtA = A.T @ A
    vals, vectors = np.linalg.eig(AtA)
    s = np.sqrt(np.abs(vals))

    idx = np.argsort(s)[::-1]
    s = s[idx]
    vectors = vectors[:, idx]

    V = vectors
    S = np.zeros((m, n))
    np.fill_diagonal(S, s)

    U = A @ V @ np.linalg.pinv(S)

    return U, S, V.T