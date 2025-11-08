def format_name(full_name):
    
    # Remove any leading/trailing spaces and split the name
    parts = full_name.strip().split()

    # If only one name is given, return it unchanged
    if len(parts) < 2:
        return full_name

    # Assume the last word is the last name
    first = " ".join(parts[:-1])
    last = parts[-1]

    # Return formatted name
    return f"{last}, {first}"


# --- Example usage ---
print(format_name("John Doe"))         # Output: Doe, John
print(format_name("Jane Mary Smith"))  # Output: Smith, Jane Mary
print(format_name("Alan Turing"))      # Output: Turing, Alan
print(format_name("Madonna"))          # Output: Madonna
