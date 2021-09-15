
my_set = {1.0, "Hello", (1, 2, 3)}
my_set.add(11)
print(my_set)
my_set.add("ABC")
print(my_set)

if "ABC" in my_set:
    my_set.remove("ABC")
    
print(my_set)
