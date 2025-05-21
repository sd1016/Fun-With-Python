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