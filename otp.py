def generate_key(plaintext):
    key = input('Enter Key: ')
    while (len(key) != len(plaintext)):
        print("Key lenght must be equal to the plaintext's\nPlaintext Lenght: " + str(len(plaintext)) +'\nKey lenght: ' + str(len(key)))
        key = input('Enter Key: ')
    
    return(key.upper())

def otp_en(plaintext):
    plaintext = plaintext.replace(' ', '')
    key = generate_key(plaintext)

    cipher = []
    for i in range(len(plaintext)):
        num = ord(plaintext[i]) - ord('A') + ord(key[i]) - ord('A')
        if num > 25:
            num -= 26
        cipher.append(num)

    encryption = ''
    for i in range(len(plaintext)):
        encryption += chr(cipher[i] + ord('A'))

    return(encryption)

def otp_dec(string):
    plainNum = []
    key = generate_key(string)
    for i in range(len(string)):
        num = ((ord(string[i]) - ord('A')) - (ord(key[i]) - ord('A')))
        if num < 0:
            num += 26

        plainNum.append(num)
    
    plaintext = ''
    for i in range(len(string)):
        plaintext += chr(plainNum[i] + ord('A'))

    return(plaintext)
