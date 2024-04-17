#!python 3

# Square root of a number

# Have the user enter in a number.  Use a try-except to see if the input
# is a valid number.  Determine the square root and use a try-except to
# catch exceptions if the number can not be square rooted
# note: Use the math.sqrt() function to determine a square root
# rather than number**(0.5) as we need to catch complex numbers as
# exceptions

"""
Sample Output
Enter a number:x
That is not a valid number
There is no square root   
Enter a number:-1
There is no square root
Enter a number:3       
The square root of 3.0 is 1.7320508075688772
"""
import math

while True:
    number = input("Enter number (type STOP to end program): ")

    if number=="STOP":
        exit()
    else:

        try:

            print("the square root of "+number+" is "+str(math.sqrt(float(number))))

        except:
            print("YOU CANT TAKE THE SQUARE ROOT OF SOTHING THAT ANT A NUMBER!!! or a negitave number")
    print("--------")