#!python3
#try...except to read an integer


inp = input("Please enter an integer")
try:
    print("Now going to try and convert to an integer")
    inp = int(inp)
    print("We have successfully converted to an integer")
    print(f"You entered {inp}")
except Exception as e:
    print("There was an error. Please try again\n")

