def string_to_ascii_list(s):
    ascii_list = [ord(char) for char in s]
    return ascii_list
def ascii_list_to_string(ascii_list):
    string = ''.join(chr(num) for num in ascii_list)
    return string
input_string = "hello"
ascii_list = string_to_ascii_list(input_string)
print("ASCII List:", ascii_list)
reconstructed_string = ascii_list_to_string(ascii_list)
print("Reconstructed String:", reconstructed_string)
