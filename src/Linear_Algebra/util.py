
# NumPy.linalg-->
# It provides functions for:
# Matrix inverse
# Determinant
# Eigenvalues
# Solving equations.




# my approach for the code
def my_approach():
        
    import numpy as np
    li=[]
    n=int(input("enter the matrix dimension"))
    for i in range(n):
        li1=list(map(int,input().split()))
        li.append(li1)

    det = np.linalg.det(li)
    print(det)
