# Write a Python program to issubset and issuperset.
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}

print(A.issuperset(B))
print(B.issuperset(A))
print(B.issubset(A))
print(C.issuperset(B))