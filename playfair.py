import string

def find(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return (i, j)
                
def generate_key():
    key = input('Enter Key: ')
    key = key.upper()
    key = key.replace('J', '')
    key = key.replace(' ', '')

    var = ''
    for char in key:
        if char not in var:
            var = var + char
    key = var

    alphabet = list(string.ascii_uppercase)
    alphabet.remove('J')

    for char in alphabet:
        if char not in key:
            key += char

    matrix = [[] for row in range(5)]

    point = 0
    for i in range(5):
        for j in range(5):
            matrix[i].append(key[point])
            point += 1
    
    return matrix

def playfair_en(string):
    key = generate_key()
    string = string.upper().replace(' ','').replace('J', '')
    print(len(string))
    arr = []
    char = ''
    for i in range(len(string)):
        if ((char == '') & (i != (len(string)-1))) | (char != string[i]) & (i != (len(string)-1)) | (i == (len(string)-1)) & (len(string)%2 == 0):
            char += string[i]
        elif (char != '') & (char == string[i]):
            char += 'X'
            arr.append(char)
            char = string[i]
        else:
            char += string[i] + 'X'

        print(char)
        if len(char) == 2:
            arr.append(char)
            char = ''

    encryption = ''
    for val in arr:
        if (find(val[0], key)[0] ==  find(val[1], key)[0]):
            for char in val:
                if (find(char, key)[1] == 4):
                    encryption += key[find(char, key)[0]][0]
                else:
                    encryption += key[find(char, key)[0]][find(char, key)[1] + 1]
        
        elif (find(val[0], key)[1] ==  find(val[1], key)[1]):
            for char in val:
                if (find(char, key)[0] == 4):
                    encryption += key[0][find(char, key)[1]]
                else:
                    encryption += key[find(char, key)[0] + 1][find(char, key)[1]]

        else:
            char1 = key[find(val[0], key)[0]][find(val[1], key)[1]]
            char2 = key[find(val[1], key)[0]][find(val[0], key)[1]]
            encryption += char1 + char2
        
    return encryption


def playfair_dec(string):
    key = generate_key()
    string = [string[i:i+2] for i in range(0, len(string), 2)]
    decrypted = ''
    for val in string:
        if (find(val[0], key)[0] ==  find(val[1], key)[0]):
            for char in val:
                if (find(char, key)[1] == 0):
                    decrypted += key[find(char, key)[0]][4]
                else:
                    decrypted += key[find(char, key)[0]][find(char, key)[1] - 1]
        
        elif (find(val[0], key)[1] ==  find(val[1], key)[1]):
            for char in val:
                if (find(char, key)[0] == 0):
                    decrypted += key[4][find(char, key)[1]]
                else:
                    decrypted += key[find(char, key)[0] - 1][find(char, key)[1]]

        else:
            char1 = key[find(val[0], key)[0]][find(val[1], key)[1]]
            char2 = key[find(val[1], key)[0]][find(val[0], key)[1]]
            decrypted += char1 + char2
            
    return(decrypted)

