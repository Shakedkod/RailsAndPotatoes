import base64, ast

def convert_dict_to_64(dict_from = {}):
    strdict = str(dict_from)
    strdict_bytes = strdict.encode("ascii")
    base64_bytes = base64.b64encode(strdict_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

#---------------------------------------------------------#

def convert_64_to_dict(base64_string, cut = None):
    base64_bytess = base64_string.encode('ascii')
    message_bytess = base64.b64decode(base64_bytess)
    message = message_bytess.decode('ascii')
    return_dict = ast.literal_eval(message)
    final_dict = return_dict[cut] if cut != None else return_dict
    return final_dict