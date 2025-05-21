def sum_numbers_in_list(numbers):
    total = 0
    for num in numbers:
        total += num  # This line assumes 'num' is a number
    return total

# Scenario 1: Correct usage
my_list = [1, 2, 3]
print(f"Sum of my_list: {sum_numbers_in_list(my_list)}")

# Scenario 2: Incorrect usage - a type-related error waiting to happen
# There's no compile-time check to prevent 'numbers_with_string' from being passed
numbers_with_string = [1, 2, "three", 4]
print(f"Sum of numbers_with_string: {sum_numbers_in_list(numbers_with_string)}")
# sum_numbers_in_list(numbers_with_string): When this function is called, Python executes the code line by line.
# It starts summing 1 + 2.
# When it gets to "three", it tries to perform 2 + "three".
# At this exact moment, Python raises a TypeError because you cannot add an integer and a string.

# the crucial point here is that Python doesn't know there's a 
# problem until it tries to execute the total += num line with incompatible types. 
# If this function call is in a rarely executed part of your code, or if the erroneous input only occurs 
# under specific conditions, the bug might not be discovered until your program is running in production, potentially leading to crashes or incorrect results.

