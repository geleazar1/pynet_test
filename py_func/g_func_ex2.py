#!/usr/bin/env python 
def my_func(x, y, z=20):
    return (x + y + z)
# function calls
print()
return_val = my_func(10, 20, 30)
print(f"Calling with three positinal args: {return_val}")
#Next names arg call
return_val = my_func(x=10, y=20)
print(f"Calling with named args: {return_val}")
# one positional and 2 named
return_val = my_func(10, z=13, y=20)
print(f"Calling one positonal and 2 named: {return_val}")
# use 3 strings
return_val = my_func("hello", "there", "world")
print(f"Calling one positonal and 2 named: {return_val}")
#using list
return_val = my_func(x=["x"], y=["y"], z=["z"])
print(f"Calling with 3 lists: {return_val}")
print()                                   

my_list = [1, 2, 3]
return_val = my_func(*my_list)
print(f"Using *args in the call: {return_val}")
# create dictionary with 3 keys and use **kwargs for calling
my_dict = {"x" : 100, "y" : 200, "z" : 300}
return_val = my_func(**my_dict)
print(f"Using **kwargs in the call: {return_val}")

