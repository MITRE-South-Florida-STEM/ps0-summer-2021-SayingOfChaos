import math

# 1. Ask the user to enter a number "x"
x = float(input("Enter a value for x: "))

# 2. Ask the user to enter a number "y"
y = float(input("Enter a value for y: "))

# 3. Prints out the number "x" raised to the power "y"
print("\n" + "\"x\" raised to the power \"y\" = " + str(x ** y) + "\n")

# 4. Prints out the log (base 2) of "x"
print("Log base 2 of \"x\" = " + str(math.log(x,2)) + "\n")