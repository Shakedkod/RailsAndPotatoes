import base64

def convert_64_to_binary(base64_string):
    encoded = base64_string.encode("ascii")
    decoded_data = base64.decodebytes(encoded)
    binary_string = "".join(["{:08b}".format(x) for x in decoded_data])
    return binary_string, decoded_data

#-----------------------------------------------------------------------------#

def convert_binary_to_64(decoded_data):
    encode = base64.encodebytes(decoded_data)
    encodeplus0 = str(encode)
    base64_string = encodeplus0.replace("b'", "", 1).replace("'", "").replace(r"\n", " ").replace("= ", "=")
    return base64_string
