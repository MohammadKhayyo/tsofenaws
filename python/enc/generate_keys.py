import random


def GenerateKey():
    str_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    list_alphabet = list(str_alphabet)
    list_shuffled = list_alphabet.copy()
    random.shuffle(list_shuffled)
    str_enc = ''.join(list_shuffled)
    dic_enc = {str_alphabet[i]: str_enc[i] for i in range(len(str_alphabet))}
    dic_dec = {value: key for key, value in dic_enc.items()}
    return dic_enc, dic_dec
