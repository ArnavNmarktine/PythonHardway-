from sys import argv

script,filename=argv 

print(f"We're going to erase {filename}.")
print("If you dont want that, hit CTRL-c(^C).")
print("If you dont want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename,'w')



print("Opening the file...")
target.turncate()

print("Now i am going to ask you for three lines.")


line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()