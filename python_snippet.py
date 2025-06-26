def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def main():
    with open("ciphertext.txt", "r") as f:
        encrypted = f.read().strip()

    decrypted_caesar = caesar_decrypt(encrypted, 3)
    print("Decrypted Base64 string:")
    print(decrypted_caesar)

    # Optional: auto-decode Base64
    try:
        import base64
        # Add padding if missing
        padding = 4 - (len(decrypted_caesar) % 4)
        if padding != 4:
            decrypted_caesar += "=" * padding
        decoded = base64.b64decode(decrypted_caesar).decode()
        print("\nDecoded mission statement:")
        print(decoded)
    except Exception as e:
        print("\nBase64 decode failed. You may need to decode manually.")
        print(str(e))

if __name__ == "__main__":
    main()