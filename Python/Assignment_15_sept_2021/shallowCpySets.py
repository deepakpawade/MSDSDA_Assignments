# Write a Python program to create a shallow copy of sets.
my_set = {1, 2, 3}
my_set2 = {1.0, "Hello", (1, 2, 3)}
set3 = my_set.copy()
print(set3)