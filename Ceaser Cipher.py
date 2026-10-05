def ceaser_encrypt(plaintext,key):
    result=""
    for ch in plaintext.upper():
        if ch.isalpha():
            result+=chr((ord(ch) - ord('A') + key)%26 + ord('A'))
        else:
            result+=ch
    return result

def ceaser_decrypt(ciphertext,key):
    return ceaser_encrypt(ciphertext,26 - key)

if __name__ == "__main__":
    plaintext = input("Enter the text :")
    key = int(input("Enter the key :"))
    cipher = ceaser_encrypt(plaintext,key)
    plain = ceaser_decrypt(cipher,key)
    print(f"Plaintext : {plaintext}")
    print(f"Key : {key}")
    print(f"Ciphertext : {cipher}")
    print(f"Decrypted : {plain}")
