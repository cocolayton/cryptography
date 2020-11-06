# import necessary libraries
import string
import binascii
import random
import math

#######################################################################################################
# Caesar Cipher

"""
    This helper function creates a dictionary with each letter of the alphabet as keys and
    their corresponding offset letter (ie. if offset_num = 3 then dict[A] = D)

    Arguments: int, string
    Returns: dictionary
"""
def get_offset_letters(offset_num, alphabet):
    alphabet_length = len(alphabet)

    # dictionary that will hold the shifted value of each letter
    offset_letters = {}
    
    # get actual offset_num if it's originally greater than alphabet length
    if offset_num > alphabet_length:
        offset_num = offset_num % alphabet_length
    
    # this value is the index in the alphabet at which wrapping begins
    wrap_point = alphabet_length - offset_num
    
    # for each letter get its corresponding shifted letter
    for index in range(alphabet_length):
        if index < wrap_point:
            offset_letters[alphabet[index]] = alphabet[index + offset_num]
        else:
            offset_letters[alphabet[index]] = alphabet[index - wrap_point]

    return offset_letters

"""
    This function takes in a string and encrypts it by exchanging each letter for the letter in the
    alphabet that is at index = original index + offset.

    Arguments: string, integer
    Returns: string
"""
def encrypt_caesar(plaintext, offset):
    # string of uppercase letters in the alphabet
    alphabet = string.ascii_uppercase

    offset_letters = get_offset_letters(offset, alphabet)

    encrypted_string = ""

    # if text empty return nothing, otherwise get each letter's corresponding shifted letter
    if plaintext == "":
        return ""
    else:
        for character in plaintext:
            if character in alphabet:
                encrypted_string = encrypted_string + offset_letters[character]
            else:
                # if not a letter but a character (!, ?, etc.) then don't change it
                encrypted_string = encrypted_string + character

        return encrypted_string


"""
    This function takes in a string and decrypts it by exchanging each letter for the letter in the alphabet
    that is at index = original index - offset (ie. reverting each letter back to the original letter).

    Arguments: string, integer
    Returns: string
"""
def decrypt_caesar(ciphertext, offset):
    # string of uppercase letters in the alphabet
    alphabet = string.ascii_uppercase

    offset_letters = get_offset_letters(offset, alphabet)

    # these lists will be used to get the key in the dictionary from a given value
    # ie. if the value is C (the encoded letter) and offset is three then want the key (letter A)
    normal_letters = list(offset_letters.keys()) 
    encoded_letters = list(offset_letters.values()) 
  
    decrypted_string = ""

    # if text empty return nothing, otherwise get each letter's corresponding shifted letter
    if ciphertext == "":
        return ""
    else:
        for character in ciphertext:
            if character in alphabet:
                decrypted_string = decrypted_string + normal_letters[encoded_letters.index(character)]
            else:
                # if not a letter but a character (!, ?, etc.) then don't change it
                decrypted_string = decrypted_string + character

        return decrypted_string



#######################################################################################################
# Vigenere Cipher

"""
    This helper funcion takes in a letter from the plaintext and the corresponding key letter and adds their
    alphabet indices to get the index of the encrypted letter (alphabet string used to get indices)

    Arguments: string, string, string
    Returns: int
"""
def get_new_encrypted_letter_index(text_char, key_char, alphabet):
    text_char_index = alphabet.find(text_char)
    key_char_index = alphabet.find(key_char)

    encrypted_char_index = text_char_index + key_char_index

    return encrypted_char_index

"""
    This helper function takes in the index of the encrypted letter and a string of the alphabet letters
    and returns the corresponding encrypted letter in the alphabet with wrapping accounted for.

    Arguments: int, string
    Returns: string
"""
def get_encrypted_letter(encrypted_char_index, alphabet):
    alphabet_length = len(alphabet)
    alphabet_max_index = len(alphabet) - 1

    # check if need to wrap back to the start of the alphabet
    if encrypted_char_index <= alphabet_max_index:
        return alphabet[encrypted_char_index]
    else:
        wrapped_index = encrypted_char_index - alphabet_length
        return alphabet[wrapped_index]


"""
    This function takes in a string (plaintext) and a key word and encrypts the plaintext by determing
    the index of the encrypted letter in the alphabet, and retreiving that corresponding letter.

    Arguments: string, string
    Returns: string
"""
def encrypt_vigenere(plaintext, keyword):
    # string of uppercase letters in the alphabet
    alphabet = string.ascii_uppercase

    # keep track of key index in case need to repeat the key work to match plaintext length
    key_index = 0

    encrypted_text = ""

    # get the alphabet index of the letter in the plaintext and the corresponding keyword letter 
    for index in range (len(plaintext)):
        text_char = plaintext[index]

        # check if need to repeat the keyword
        if key_index < (len(keyword)):
            key_char = keyword[key_index]
            key_index += 1
        else:
            key_index = 0
            key_char = keyword[key_index]
            key_index += 1

        # get the encrypted letter
        encrypted_char_index = get_new_encrypted_letter_index(text_char, key_char, alphabet)
        encrypted_letter = get_encrypted_letter(encrypted_char_index, alphabet)


        encrypted_text = encrypted_text + encrypted_letter

    return encrypted_text


"""
    This helper function takes in a letter from the encrypted text and the corresponding key letter and
    subtracts the alphabet index of the key letter from the alphabet index of the encrypted letter
    (alphabet string used to get indices)

    Arguments: string, string
    Returns: int
"""
def get_new_decrypted_letter_index(cipher_char, key_char, alphabet):
    cipher_char_index = alphabet.find(cipher_char)
    key_char_index = alphabet.find(key_char)

    decrypted_char_index = cipher_char_index - key_char_index

    return decrypted_char_index

"""
    This helper function takes in the index of the decrypted letter and a string of the alphabet letters
    and returns the corresponding decrypted letter in the alphabet with wrapping accounted for

    Arguments: int, string
    Returns: string
"""
def get_decrypted_letter(decrypted_char_index, alphabet):
    alphabet_length = len(alphabet)

    # check if need to wrap to the back of the alphabet (index of A = 0)
    if decrypted_char_index >= 0:
        return alphabet[decrypted_char_index]
    else:
        wrapped_index = alphabet_length + decrypted_char_index # add because decrypted_char_index will be negative
        return alphabet[wrapped_index]


"""
    This function takes in a string (ciphertext) and a key word and decrypts the ciphertext by determining 
    the index of the decrypted letter in the alphabet and retrieving the corresponding letter.

    Arguments: string, string
    Returns: string
"""
def decrypt_vigenere(ciphertext, keyword):
    # string of uppercase letters in the alphabet
    alphabet = string.ascii_uppercase

    # keep track of key index in case need to repeat the key work to match plaintext length
    key_index = 0

    decrypted_text = ""

    # get the alphabet index of the letter in the ciphertext and the corresponding keyword letter
    for index in range(len(ciphertext)):
        cipher_char = ciphertext[index]

        # check if need to repeat the keyword
        if key_index < (len(keyword)):
            key_char = keyword[key_index]
            key_index += 1
        else:
            key_index = 0
            key_char = keyword[key_index]
            key_index += 1

        # get the decrypted letter
        decrypted_char_index = get_new_decrypted_letter_index(cipher_char, key_char, alphabet)
        decrypted_letter = get_decrypted_letter(decrypted_char_index, alphabet)
        

        decrypted_text = decrypted_text + decrypted_letter

    return decrypted_text

#######################################################################################################
# Merkle-Hellman Knapsack Cryptosystem

"""
    This helper function creates a super increasing sequence (starting at 1) with n = 8 numbers
    in the tuple

    Arguments: int
    Returns: tuple
"""
def get_W(n=8):
    W = []
    W.append(1) # starting small number for increasing list
    
    count = 1 # 1 because just appended the first number

    while count < n:
        # get total of numbers in the list so far
        total = 0
        for num in W:
            total = total + num

        # generate next random number in super increasing sequence
        rand_num = random.randint(total + 1, total*2)
        W.append(rand_num)
        count += 1

    return tuple(W)

"""
    This helper function takes in the super increasing sequence, W, and returns what would be the next
    generated number in the sequence (ie. a number, Q, that is greater than the sum of all the elements in W)

    Arguments: tuple
    Returns: int
"""
def get_Q(W):
    total = 0

    # get sum of all elements in W
    for num in W:
        total = total + num

    # generate a random integer greater than that sum
    Q = random.randint(total + 1, total*2)

    return Q

"""
    This helper function finds some integer R such that GCD(R, Q) == 1

    Arguments: int
    Returns: int
"""
def get_R(Q):
    # generate random value for R between 2 and Q-1
    R = random.randint(2, Q-1)

    while (math.gcd(R, Q) != 1):
        R = random.randint(2, Q-1)

    return R

"""
    This function generates a private key given n = 8
    (charcters are 8 bit messages so W needs only n = 8 elements)  

    Arguments: int
    Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
"""
def generate_private_key(n=8):
    W = get_W()
    Q = get_Q(W)
    R = get_R(Q)
    private_key = (W, Q, R)
    
    return private_key

"""
    This function generates a public key (B) given a private key (W, Q, R), such that
    B = (b_1, b_2, … b_n) where b_i = R * w_i mod Q

    Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
    Returns: tuple B - a length-n tuple of integers
"""
def create_public_key(private_key):
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]

    B = [] # the public key
    
    for num in W:
        B.append(R * num % Q)

    return tuple(B)



"""
    This helper function takes in the binary representation of a character and a public key and
    returns the encrypted integer version of the character

    Arguments: list of integers (binary), tuple
    Returns: int
"""
def get_cipher_num(binary_list, public_key):
    C = 0

    for num in (range(len(binary_list))):
        C = C + (public_key[num] * binary_list[num]) # multiply key value by corresponding binary # (0 or 1)

    return C


"""
    This function takes in a string (plaintext) with a public key and uses the key values to
    encrypt the string.

    Arguments: string, tuple B
    Returns: list of integers
"""
def encrypt_mhkc(plaintext, public_key):
    encryption = []

    # if plaintext is empty return empty list
    if (plaintext == ""):
        return encryption
    
    for letter in plaintext:
        # get ascii value of letter and convert to binary
        ascii_value = ord(letter)
        binary = format(ascii_value, '08b') # keep leading zeros by ensuring all 8 bits are included
        binary_list = [int(x) for x in binary] # turns string into a list

        # get encrypted version of character
        C = get_cipher_num(binary_list, public_key)

        encryption.append(C)

    return encryption

"""
    This helper function uses Euclid's extended algorithm to find the modular multiplicative inverse
    of 'a' under modulor 'm'


    Based on equation: ax + by = gcd(a, b)
        
    Replace b with m because want to find the multiplicative inverse of ‘a’ under ‘m’
    And we know gcd(a, b) = 1 because a and b are coprime prime:
        ax + my = 1

    Take modulo of both sides:
        ax + my = 1 (mod m)

    Remove my since my(mod m) is 0 for integer y:
        ax = 1 (mod m)

    x is the multiplicative inverse of 'a' so that's what is calculated

    
    I got this code from GeekForGeeks: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/

    Arguments: int, int
    Returns: int
"""
def modInverse(a, m) : 
    m0 = m
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
        place_holder = m 
  
        # m is remainder now, process same as Euclid's algo 
        m = a % m 
        a = place_holder 
        place_holder = y 
  
        # Update x and y 
        y = x - q * y 
        x = place_holder
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x # the multiplicative inverse of 'a'

"""
    This helper function takes in R and Q (ints) and a character (really an integer) from the encrypted
    string and calculates the inital target value (called C' in this method)later used to determine what
    indices of W are needed to calculate the ascii value of the encrypted character.

    Arguments: int, int, string
    Returns: int
"""
def get_cprime(R, Q, cipher_char, n = 8):
    #equation: C' = C * R' % Q
    r_prime = modInverse(R, Q)
    c_prime = cipher_char * r_prime % Q
    return c_prime

"""
    This helper function what indexes of W are needed to calculate the ascii value of the
    encrypted character.

    Arguments: int, tuple
    Returns: list of integers
"""
def get_W_values(cprime, W, n = 8):
    target = cprime

    indices_list = []

    for index in (reversed(range(n))):
        # if the value of W at that index is less than the target, add that index to the list
        if W[index] <= target:
            indices_list.append(index+1) # +1 because W goes from 1-8 not 0-7 so need to get correct index
            target = target - W[index]

        # once enough numbers have been subtracted and target = 0, you have all the necessary indices
        if target == 0:
            return indices_list

"""
    This function determines what indexes of W are needed to calculate the ascii value of
    the encrypted character.

    Arguments: list of integers, private key (W, Q, R) with W a tuple
    Returns: bytearray or str of plaintext
"""
def decrypt_mhkc(ciphertext, private_key):
    n = 8 # the number of bits used to encode/decode each character in the message

    decryption_bytes = [] # list that will hold calculated ascii values from ciphertext

    # if ciphertext is empty list return empty string
    if ciphertext == []:
        return ""

    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]

    for cipher_char in ciphertext:
        cprime = get_cprime(R, Q, cipher_char)
        indices_list = get_W_values(cprime, W)

        ascii_num = 0
        
        # calculate the ascii number of the character (really integer) in ciphertext
        for index in indices_list:
            ascii_num = ascii_num + (2**(n-index))

        decryption_bytes.append(ascii_num)

    # convert ascii numbers to letters
    message = ""
    for value in decryption_bytes:
        message = message + chr(value)

    return message


def main():
    pass
    # Testing Cesear
    #encrypt = encrypt_caesar("?AB", 492)
    #decrypt = decrypt_caesar(encrypt, 492)
    #print(decrypt, encrypt)

    # Testing vingeere
    #ciphertext = encrypt_vigenere("", "ALASDKJF")
    #decrypted = decrypt_vigenere(ciphertext, "ALASDKJF")
    #print(decrypted, ciphertext)

    # Testing MHKC
    #plaintext = "PUMPKIN"
    #private_key = generate_private_key()
    #public_key = create_public_key(private_key)
    #private_key = ((10, 14, 35, 115, 248, 677, 1413, 3644), 10242, 5)
    #public_key = (50, 70, 175, 575, 1240, 3385, 7065, 7978)
    #encrypt = encrypt_mhkc(plaintext, public_key)
    #decrypt = decrypt_mhkc(encrypt, private_key)
    #print(encrypt)
    #print(decrypt)

    

if __name__ == "__main__":
    main()
