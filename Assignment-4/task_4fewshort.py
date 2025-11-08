# Few-shot examples to guide the function

# Example 1
# Input: "apple"
# Vowels: a, e
# Output: 2

# Example 2
# Input: "banana"
# Vowels: a, a, a
# Output: 3

# Now the function implementation
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Test cases
test_strings = [
    "apple",
    "banana",
    "Hello World",
    "OpenAI",
    "Python Programming"
]

for string in test_strings:
    print(f"Vowels in '{string}': {count_vowels(string)}")
