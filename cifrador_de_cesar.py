encrypt = 1
decrypt = 0

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == encrypt else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data


key = 3
original = 'Cursaremos sistemas de informação'
print('  Original:', original)
ciphered = caesar(original, key, encrypt)
print('Encriptada:', ciphered)
plain = caesar(ciphered, key, decrypt)
print('Decriptada:', plain)
