# this one is like your script with argv 
def print_two(*args):
    arg1, arg2 =args 
    print(f"arg1:{arg1},arg2:{arg1}")

# okay, that *args is actually, pointless , we can just do this 

def print_two_again(arg1, arg2):
    print(f"arg1 :{arg1}")

#this one takes no argument 

def print_one(arg1):
    print(f"arg1:{arg1}")

# this one takes no argumnets

def print_none():
    print("I got nothin'.")
 
print_two("Zed", "Shaw")``
print_two_again("Zed", "Shaw")
print("First!")
print_none()