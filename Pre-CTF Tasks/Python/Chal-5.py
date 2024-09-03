def string_to_ascii_list(s):
    return [ord(char) for char in s]
def ascii_list_to_string(ascii_list):
    return ''.join(chr(ascii_value) for ascii_value in ascii_list)
original_string = "Hello, World!"
ascii_list = string_to_ascii_list(original_string)
reconstructed_string = ascii_list_to_string(ascii_list)
print("Original string:", original_string)
print("ASCII list:", ascii_list)
print("Reconstructed string:", reconstructed_string)
