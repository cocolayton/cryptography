# Caesar Cipher
# Arguments: string, integer
# Returns: string

def get_offset_letters(offset_num, alphabet):
    # dictionary that will hold the shifted value of each letter in the alphabet given an offset number
    offset_letters = {}
    
    #range represents letters that will not need to loop (ie if offset is 3 the go up to range 22)
    range_for_first_loop = 26-offset_num
    for index in range(range_for_first_loop):
        offset_letters[alphabet[index]] = alphabet[index + index]

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

#######################################################################################################
# Vigenere Cipher

def get_new_encrypted_letter_index(text_char, key_char):
    alphabet = string.ascii_uppercase

    text_char_index = alphabet.find(text_char)
    key_char_index = alphabet.find(key_char)

    encrypted_char_index = text_char_index + key_char_index

    return encrypted_char_index


def get_encrypted_letter(encrypted_char_index):
    alphabet = string.ascii_uppercase
    if encrypted_char_index < 24:
        return alphabet[encrypted_char_index]
    else:
        wrapped_index = encrypted_char_index - 26 #subtract 25 not 24 because index starts at zero
        return alphabet[wrapped_index]


def get_new_decrypted_letter_index(cipher_char, key_char):
    alphabet = string.ascii_uppercase

    cipher_char_index = alphabet.find(cipher_char)
    key_char_index = alphabet.find(key_char)

    decrypted_char_index = key_char_index - cipher_char_index


def get_decrypted_letter(decrypted_char_index):
    alphabet = string.ascii_uppercase

    if decrypted_char_index > 0:
        return alphabet[decrypted_char_index]
    else:
        wrapped_index = 26 - decrypted_char_index
        return alphabet[wrapped_index]

# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    key_index = 0
    encrypted_text = ""

    for index in range len(plaintext):
        text_char = plaintext[index]

        if key_index < len(keyword)
            key_char = keyword[key_index]
            key_index += 1
        else:
            key_index = 0
            key_char = keyword[key_index]
            key_index += 1

        encrypted_char_index = get_new_encrypted_letter_index(text_char, key_char)
        encrypted_letter = get_encrypted_letter(encrypted_char_index)
        encrypted_text = encrypted_text + encrypted_letter


    return encrypted_text


# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    key_index = 0
    encrypted_text = ""

    for index in range len(ciphertext):
        cipher_char = ciphertext[index]

        if key_index < len(keyword)
            key_char = keyword[key_index]
            key_index += 1
        else:
            key_index = 0
            key_char = keyword[key_index]
            key_index += 1

        decrypted_char_index = get_new_decrypted_letter_index(cipher_char, key_char)
        decrypted_letter = get_decrypted_letter(decrypted_char_index)
        decrypted_text = decrypted_text + decrypted_letter

    return decrypted_text

#######################################################################################################

# Merkle-Hellman Knapsack Cryptosystem


def get_W(n=8):
    W = []
    W.append(1) # starting small number for increasing list
    
    count = 1 # going to add 8 numbers

    for count < n:
        # get total of numbers in the list so far
        total = 0
        for num in W:
            total = total + num

        rand_num = random.randint(total + 1, total*2)
        W.append(rand_num)
        count += 1

    return tuple(W)

def get_Q(W):
    total = 0
    for num in W:
        total = total + num

    Q = random.randint(total + 1, total*2)
    return Q

def get_R(Q):
    R = random.randint(2, Q-1)
    if math.gcd(Q, R) == 1:
        return R
    else:
        get_R(Q)

def get_B(W, Q, R):
    B = []

    for num in W:
        B.append(R*num%Q)

    return tuple(B)

def get_key_elements():
    W = get_W()
    Q = get_Q(W)
    R = get_R(Q)
    B = get_B(W, Q, R)

    return (W, Q, R, B)

# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    W, Q, R, B = get_key_elements()
    private_key = (W, Q, R)

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    W, Q, R, B = get_key_elements()
    public_key = B

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
