from generate_keys import GenerateKey as G_K
from Encryption_Decryption_from_to_by_key import Encryption_Decryption_from_to
from Convert_From_to_Json import Convert_from_Json, Convert_to_Json
import string


def enc_newkey(my_key):

    dic_enc, dic_dec = G_K()
    print(f"A new key called {my_key} was created")
    return dic_enc, dic_dec


def enc_load(file):
    dic_enc, dic_dec, nameKey = Convert_from_Json(file)
    if dic_enc:
        print(f"Key {nameKey} from file {file} loaded")
    return dic_enc, dic_dec, nameKey


def enc_save(file, dic_enc, dic_dec, nameKey):
    ret = Convert_to_Json(dic_enc, dic_dec, file, nameKey)
    if ret == 1:
        return ret
    print(f"Enc/Dec keys saved in {file} file")
    return ret


def Decryption(_from, _to, dic_dec):
    ret = Encryption_Decryption_from_to(dic_dec, _from, _to)
    if ret == 1:
        return ret
    print(f"File {_from} was decrypted into {_to}")
    return ret


def enc_info(nameKey, dic_enc, dic_dec, ExistSaved, *more):
    letters = string.ascii_lowercase

    print("Current key:", nameKey)
    if ExistSaved:
        print("state:", "saved in", more[0])
    else:
        print("state: not saved")
    print("Encryption:")
    print("\t", letters)
    print("\t", ''.join([value for key, value in dic_enc.items()]))
    print("Decryption:")
    print("\t", ''.join([key for key, value in dic_dec.items()]))
    print("\t", letters)


def Encryption(_from, _to, dic_enc):
    ret = Encryption_Decryption_from_to(dic_enc, _from, _to)
    if ret == 1:
        return ret
    print(f"File {_from} was encrypted into {_to}")
    return ret


Commands = {
    'info': enc_info,
    'load': enc_load,
    'newkey': enc_newkey,
    'save': enc_save,
    'dec': Decryption,
    'enc': Encryption
}


def main_cli():
    cli_end = False
    ExictKey = False
    ExistSaved = False
    dic_enc = dict()
    dic_dec = dict()
    nameKey = ''
    nameFile = ''
    while not cli_end:
        cmd_str = input('subs>')
        cmd = cmd_str.split()
        if not cmd:
            continue
        if cmd[0] == 'done':
            cli_end = True
            continue
        if cmd[0] not in Commands:
            print("Command not Found")
            continue
        if ExictKey and cmd[0] == "info":
            if not nameFile:
                ExistSaved = False
            else:
                check1, check2, check3 = Convert_from_Json(
                    nameFile, "No Print")
                if not check1 or not check2 or not check3:
                    ExistSaved = False
                    nameFile = ''
            Commands[cmd[0]](nameKey, dic_enc, dic_dec, ExistSaved, nameFile)
            continue
        if len(cmd) < 2:
            continue
        if cmd[0] == "newkey":
            dic_enc, dic_dec = Commands[cmd[0]](cmd[1])
            nameKey = cmd[1]
            ExictKey = True
            ExistSaved = False
            nameFile = ''
            continue
        if cmd[0] == "load":
            dic_enc_tmp, dic_dec_tmp, nameKey_tmp = Commands[cmd[0]](
                cmd[1])
            if not dic_dec_tmp or not dic_enc_tmp or not nameKey_tmp:
                continue
            dic_enc, dic_dec, nameKey = dic_enc_tmp, dic_dec_tmp, nameKey_tmp
            ExictKey = True
            ExistSaved = True
            nameFile = cmd[1]
            continue
        if not ExictKey:
            print("No key yet")
            continue
        if cmd[0] == "save":
            Commands[cmd[0]](cmd[1], dic_enc, dic_dec, nameKey)
            ExistSaved = True
            nameFile = cmd[1]
            continue
        if (len(cmd) < 3):
            continue
        if cmd[0] == "enc":
            Commands[cmd[0]](cmd[1], cmd[2], dic_enc)
            continue
        if cmd[0] == "dec":
            Commands[cmd[0]](cmd[1], cmd[2], dic_dec)
            continue


main_cli()
