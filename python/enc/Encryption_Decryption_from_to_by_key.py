def Encryption_Decryption_from_to(dic, _from, _to):
    str_enc = ''
    try:
        with open(_from, "r") as fm:
            str = fm.read()
            list_str = list(str)
            for letter in list_str:
                if letter in dic:
                    str_enc += dic[letter]
                else:
                    str_enc += letter
        with open(_to, "w") as ft:
            ft.write(str_enc)
    except FileNotFoundError as e:
        print(f"file not found: {e}")
        print("from Encryption_Decryption_from_to")
        return 1
    except Exception as e:
        print(f"Other error {e}")
        print("from Encryption_Decryption_from_to")
        return 1
    else:
        return 0
