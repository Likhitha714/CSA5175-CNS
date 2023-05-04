alphabet = "abcdefghijklmnopqrstuvwxyz"
key = str(input("enter a string"))
plaintext = str(input("enter a string"))
ciphertext = ""
for i in range(len(plaintext)):
    index = alphabet.index(plaintext[i])
    key_index = i % len(key)
    key_char = key[key_index]
    key_alphabet_index = alphabet.index(key_char)
    cipher_index = (index + key_alphabet_index) % 26
    ciphertext += alphabet[cipher_index]
print(ciphertext)
