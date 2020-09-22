# Caesar Cipher
# Arguments: string, integer
# Returns: string

def get_offset_letters(offset_num, alphabet):
    # dictionary that will hold the shifted value of each letter in the alphabet given an offset number
    offset_letters = {}
    
    #range represents letters that will not need to loop (ie if offset is 3 the go up to range 22)
    range_for_first_loop = 26-offset_num
    for index in range(range_for_first_loop):
        offset_letters[alphabet[index]] = alphabet[index+3]

    # letters that need to loop back to the front of the alphabet
    for index in range(offset_num):
        offset_letters[alphabet[range_for_first_loop] + index] = alphabet[index]

    return offset_letters


def encrypt_caesar(plaintext, offset):
    # string of uppercase letters
    alphabet = string.ascii_uppercase

    offset_letters = get_offset_letters(offset, alphabet)

    encrypted_string = ""

    if plaintext == "":
        return ""
    else:
        for character in plaintext:
            if character in alphabet:
                encrypted_string = encrypted_string + offset_letters[character]
            else:
                encrypted_string = encrypted_string + character # can't assume its a letter (might be ? or ! , etc.)

        return encrypted_string


# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    alphabet = string.ascii_uppercase

    offset_letters = get_offset_letters(offset, alphabet)

    # these lists will be used to get the key in the dictionary from a value (ie correct letter from the given encoded letter)
    key_list = list(my_dict.keys()) 
    val_list = list(my_dict.values()) 
  

    decrypted_string = ""

    if ciphertext == "":
        return ""
    else:
        for character in ciphertext:
            if character in alphabet:
                decrypted_string = decrypted_string + key_list[val_list.index(character)]
            else:
                decrypted_string = decrypted_string + character # can't assume its a letter (might be ? or ! , etc.)

        return decrypted_string

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    # WHAT IF GIVEN A BLANK STRING?????
    pass

if __name__ == "__main__":
    main()
