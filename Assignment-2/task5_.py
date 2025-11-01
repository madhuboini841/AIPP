def calculate_sums(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum

# Example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate sums
even_sum, odd_sum = calculate_sums(numbers)

# Print results
print(f"List of numbers: {numbers}")
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")