def is_palindrome_efficient(string):
    return string == string[::-1]
user_input = input("Enter a string: ")
if is_palindrome_efficient(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
