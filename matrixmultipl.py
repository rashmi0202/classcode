### basic subroutines for matrix operations
### written for learning git
import numpy as np
def multiply(mat1,mat2,n):
    product=np.zeros([n,n])
    for i in range(n):
      for j in range(n):
        for k in range(n):
            product[i][j]=mat1[i][k]*mat2[k][j]
    return(product)
##############################################

def largest_element(mat,n):
  largest_element=100.0
  for i in range(n):
    for j in range(n):
      if(largest_element<mat[i][j]):
        largest_element=mat[i][j]
  return(largest_element)

####################################################################

## initialize two matrices
n=3
mat1=np.zeros([n,n])
mat2=np.zeros([n,n])

## assign some values
for i in range(0,n):
  for j in range(0,n):
    mat1[i][j]=i+j
    mat2[i][j]=i-j

## testing multiplication
print('')
print("testing matrix multiplication")
reference_product=np.matmul(mat1,mat2)
test_product=multiply(mat1,mat2,n)
print(reference_product-test_product)

## testing largest_element
print('')
print("testing largest element")
reference_max=np.amax(mat1)
test_max=largest_element(mat1,n)
print(test_max-reference_max)
