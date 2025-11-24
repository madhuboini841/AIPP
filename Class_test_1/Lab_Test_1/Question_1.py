def factorial(n):
    """
    Calculate factorial using a loop.
    - Returns 1 for 0
    - Prints an error message and returns None for negative numbers
    - Uses an iterative loop (no recursion)
    """
    if not isinstance(n, int):
        print("Error: factorial is only defined for integers")
        return None
    if n < 0:
        print("Error: factorial is not defined for negative numbers")
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    tests = [-3, 0, 1, 5, 10]
    for t in tests:
        res = factorial(t)
        if res is None:
            print(f"factorial({t}) -> error")
        else:
            print(f"factorial({t}) = {res}")

# Example output when run:
# Error: factorial is not defined for negative numbers
# factorial(-3) -> error
# factorial(0) = 1
# factorial(1) = 1
# factorial(5) = 120
# factorial(10) = 3628800
