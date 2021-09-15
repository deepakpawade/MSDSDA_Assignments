setx = {1, 2, 3, "Hello"}
sety = {1.0, "Hello", (1,2,3)}
print("Original set elements:")
print(setx)
print(sety)
print("\ndifference of two said sets: first x-y then y-x")
result = setx.difference(sety)
print(result)

result = sety.difference(setx)
print(result)