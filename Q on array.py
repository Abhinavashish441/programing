A=[0,1,0,3,0,5,9,6,]
B=[2,4,7]
#                          A and B is given by user
#                          Now we have to fill empty shell of A with Bth Element
#                          Final Array must be sorted also 
#                          0 repesent emapty shell
C= A+B
print(C)
C.sort()
print(C)
X=[]
for i in range(len(C)):
    if C[i] != 0:
        X.append(C[i])
print(X)
