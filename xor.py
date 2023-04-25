def xor(text, key):
    result = ""
    for char in text:
        char_value = ord(char)
        key_value = ord(key)
        xor_result = char_value ^ key_value
        result += chr(xor_result)
    return result
text = input("Text: ")
key = input("Key: ")

encrypted_text = xor(text, key)

print(encrypted_text)