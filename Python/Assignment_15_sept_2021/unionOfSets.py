setx = {1, 2, 3, "Hello"}
sety = {1.0, "Hello", (1,2,3)}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
result = setx.union(sety)
print(result)