import numpy as np

def diagonal_product(arr: np.ndarray) -> int:
    diag_elements = np.diag(arr)
    return int(np.prod(diag_elements))


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(diagonal_product(arr))