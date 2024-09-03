def encrypt_text(text):
    key_sequence = [0x01, 0x23, 0x45, 0x67, 0x89]
    ascii_values = [ord(char) for char in text]
    encrypted_values = []
    for i, value in enumerate(ascii_values):
        key = key_sequence[i % len(key_sequence)]
        encrypted_value = value ^ key
        encrypted_values.append(encrypted_value)
    return encrypted_values
text = "Hello, World!"
encrypted_list = encrypt_text(text)
print(encrypted_list)
