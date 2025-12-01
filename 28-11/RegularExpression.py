
import re

def remove_special_chars(text):
    # Keep only letters, digits, and spaces
    cleaned = re.sub(r'[^A-Za-z0-9 ]', '', text)
    return cleaned

# Example usage
input_str = "Hello@World! Python#2025$"
result = remove_special_chars(input_str)
print("Original:", input_str)
print("Cleaned:", result)
