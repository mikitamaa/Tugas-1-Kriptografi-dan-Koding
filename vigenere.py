def generate_key(plaintext):
    key = input('Enter Key: ')
    if (len(key) != len(plaintext)):
        pointer = 0
        while len(key) != len(plaintext):
            key += plaintext[pointer]
            pointer += 1
            if pointer == len(plaintext):
                pointer = 0
    
    print('\nHere is your key: ' + key)
    return(key)

def vigenere_std(plaintext):
    cipher = ''
    plaintext = plaintext.replace(' ', '').upper()
    key = generate_key(plaintext)
    for i in range(len(plaintext)):
        cipher += chr(((ord(plaintext[i])-ord('A')) + (ord(key[i])-ord('A')))%26 + ord('A'))

    return(cipher)


def vigenere_autokey(plaintext, key):
    autokey = key
    plaintext = plaintext.replace(' ', '')
    if (len(plaintext) > len(autokey)):
        autokey += plaintext[0:(len(plaintext)-len(key))]
    cipher = vigenere_std(plaintext, autokey)

    return(cipher, autokey)

def vigenere_dec(string):
    key = input('Enter Key: ')
    plaintext = ''
    for i in range(len(string)):
        plaintext += chr((ord(string[i]) - ord(key[i]) + 26) % 26 + ord('A'))
    return(plaintext)