
import numpy as np

decision = 1

while(decision):
	rA, cA = input("Enter size of coefficient matrix: ").split(" ")
	rA, cA = int(rA), int(cA)
	A = []
	for i in range(rA):
		elements = input("Enter Row {}: ".format(i)).split(" ")
		A.insert(i, [int(j) for j in elements])
	A = np.array(A)

	B = input("Enter right side column matrix: ").split(" ")
	B = [[int(k)] for k in B]
	B = np.array(B)
	rB, cB = B.shape

	if((rA == cA and np.linalg.det(A) != 0) and rA == rB and cB == 1):
		print("Gaussian Elimination with partial pivoting can be performed!")
		decision = 0
	else:
		print("Either matrix is not square or determinant is zero or size of B is not correct!")
		exit

print("coefficient Matrix: \n", A)
print("Right Side Matrix: \n", B)

AU = np.concatenate((A,B), axis=1)
print("Augmented Matrix: \n", A)

rk_A = np.linalg.matrix_rank(A)
rk_AU = np.linalg.matrix_rank(AU)

if(rk_AU == rk_A and rk_A == rA):
	print("System has unique solution as rank of Augmented matrix and rank of coefficient matrix are equal to number of rows of the matrix!")
else:
	print("This System cannot be solved using Gauss Method")
	exit


