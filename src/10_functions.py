# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    return True if n % 2 == 0 else False

print(is_even(10))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
print("Even!" if is_even(num) else "Odd")
# YOUR CODE HERE

