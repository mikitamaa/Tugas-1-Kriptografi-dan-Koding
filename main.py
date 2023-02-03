from vigenere import *
from playfair import *
from otp import *

def inputype():
    print('Choose a type of the plaintext: ')
    print('1.   Manual Input')
    print('2.   .txt File')
    option = input('Enter Option: ')
    if (option == '1'):
        string = input('Enter String: ')
    
    elif (option == '2'):
        path = input('Enter File Path: ')
        string = open(path, "r").read()
        
    return(string)

running = True
while running:
    print('\nChoose an Encryption to Do: ')
    print('1.   Vigenere')
    print('2.   Vigenere Extended (Autokey)')
    print('3.   Playfair')
    print('4.   One Time Pad')
    print('\nOr \n')
    print('Choose an Decryption to Do: ')
    print('5.   Vigenere')
    print('6.   Playfair')
    print('7.   One Time Pad')
    print('\n8.    Exit!')

    option = input('Enter Option: ')
    if (option == '1'):
        string = inputype()
        print('Cipher: '+ vigenere_std(string.upper()))
    
    elif (option == '2'):
        string = inputype()
        key = input('Enter Key: ')
        print('Cipher: '+ vigenere_autokey(string.upper()), key)

    elif (option == '3'):
        string = inputype()
        print('Cipher: '+ playfair_en(string.upper()))
    
    elif (option == '4'):
        string = inputype()
        print('Cipher: '+ otp_en(string.upper()))

    elif (option == '5'):
        string = inputype()
        print('Plaintext: '+ vigenere_dec(string.upper()))

    elif (option == '6'):
        string = inputype()
        print('Plaintext: '+ playfair_dec(string.upper()))

    elif (option == '7'):
        string = inputype()
        print('Plaintext: '+ otp_dec(string.upper()))

    elif (option == '8'):
        running = False