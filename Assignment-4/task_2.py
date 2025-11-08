def cm_to_inches(cm):
    """Convert centimeters to inches."""
    inches = cm / 2.54
    return inches

# Example usage
if __name__ == "__main__":
    cm_value = float(input("Enter value in centimeters: "))
    inches_value = cm_to_inches(cm_value)
    print(f"{cm_value} cm is equal to {inches_value} inches.")