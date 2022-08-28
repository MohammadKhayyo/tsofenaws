import json


def Convert_to_Json(dic_enc, dic_dec, file, nameKey):
    dic = {"enc": dic_enc, "dec": dic_dec, "nameKey": nameKey}
    json_object = json.dumps(dic)
    try:
        with open(file, "w") as f:
            f.write(json_object)
    except FileNotFoundError as e:
        print(f"file not found: {e}")
        return 1
    except Exception as e:
        print(f"Other error {e}")
        return 1
    return 0


def Convert_from_Json(file, *more):
    try:
        with open(file, "r") as f:
            json_object = f.read()
            dic = json.loads(json_object)
            return dic["enc"], dic["dec"], dic["nameKey"]
    except FileNotFoundError:
        print("No such key")
        return (None, None, None)
    except ValueError:
        print("No such key")
        return (None, None, None)
    except Exception as e:
        if not more:
            print(f"Other error {e}")
        return (None, None, None)
