def caesar_cipher(text, key, decrypt=False):
    """Encrypts or decrypts text using the Caesar cipher with the given key"""
    if decrypt:
        key = -key 
    cipher_text = ""
    for char in text:
        if char.isalpha(): 
          
            char_code = ord(char.lower())  
            char_code = (char_code - 97 + key) % 26 + 97  
            cipher_text += chr(char_code)  
        else:
            cipher_text += char 
    return cipher_text


plain_text = "Hello"
key = 4
cipher_text = caesar_cipher(plain_text, key)
print("Cipher Text:", cipher_text)
decrypted_text = caesar_cipher(cipher_text, key, decrypt=True)
print("Decrypted Text:",decrypted_text)
