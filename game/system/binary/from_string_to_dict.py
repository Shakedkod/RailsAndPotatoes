global the_final_dict, start_string, start_int, start_dict, start_list, start_true, start_false, key, string, listt, dictt, integer, what_key, dictt_staff, listt_staff
the_final_dict = {}
start_string = False
start_int = False
start_dict = False
start_list = False
start_true = False
start_false = False
key = True
string = ""
listt = []
dictt = {}
integer = 0
what_key = ""
dictt_staff = {
    "key": True,
    "what_key": "",
    "int": 0,
    "str": "",
    "list": [],
    "start int": False,
    "start str": False,
    "start list": False,
    "start true": False,
    "start false": False
}
listt_staff = {
    "int": 0,
    "str": "",
    "dict": {},
    "start int": False,
    "start str": False,
    "start dict": False,
    "start true": False,
    "start false": False
}

def listttttt_for_staff(letter):
    global listt, listt_staff, start_dict, dictt, dictt_staff
    
    if letter == "]":
        if listt_staff["start int"]:
            listt.append(int(listt_staff["int"]))
        return False

    #if we need to start something
    if not listt_staff["start str"] and not listt_staff["start int"] and not listt_staff["start dict"] and not listt_staff["start true"] and not listt_staff["start false"]:
        if letter == "'": #start string
            listt_staff["start str"] = True
        
        elif letter.isdigit(): #start int
            listt_staff["start int"] = True
            listt_staff["int"] = letter
        
        elif (letter == "{") and not start_dict: #start dict
                listt_staff["start dict"] = True
                listt_staff["dict"] = {}
        
        elif letter == "T":
            listt_staff["start true"] = True
        
        elif letter == "F":
            listt_staff["start false"] = True
    #############################################
    #*----------if we started already----------*#
    #############################################
    #string
    elif listt_staff["start str"]:
        if letter == "'": #if we need to end the string
            listt.append(listt_staff["str"])
            listt_staff["str"] = ""
            listt_staff["start str"] = False
        else: #if we dont have to end the string
            listt_staff["str"] += letter
    
    #integer
    elif listt_staff["start int"]:
        if letter == ",": #if we need to end the int
            listt.append(int(listt_staff["int"]))
            listt_staff["int"] = 0
            listt_staff["start int"] = False
        else: #if we dont have to end the int
            listt_staff["int"] += letter
    
    elif listt_staff["start dict"]:
        if dictttttt_for_staff(letter):
            pass
        else:
            listt_staff["start dict"] = False
            listt.append(dictt)
            dictt = {}
            dictt_staff = {
                "key": True,
                "what_key": "",
                "int": 0,
                "str": "",
                "list": [],
                "start int": False,
                "start str": False,
                "start list": False,
                "start dict": False,
                "start true": False,
                "start false": False
            }

    elif listt_staff["start true"]:
        if letter == "e":
            listt.append(True)
            listt_staff["start true"] = False
    
    elif listt_staff["start false"]:
        if letter == "e":
            listt.append(False)
            listt_staff["start false"] = False
    
    else:
        listt.append(None)
    
    return True

def dictttttt_for_staff(letter):
    global dictt, dictt_staff, start_list, listt, listt_staff
    
    if letter == "}":
        if dictt_staff["start int"]:
            dictt[dictt_staff["what_key"]] = int(dictt_staff["int"])
        return False

    #if we need to start something
    if not dictt_staff["start str"] and not dictt_staff["start int"] and not dictt_staff["start list"] and not dictt_staff["start true"] and not dictt_staff["start false"]:
        if letter == "'": #start string
            dictt_staff["start str"] = True
        
        elif letter.isdigit(): #start int
            dictt_staff["start int"] = True
            dictt_staff["int"] = letter
        
        elif letter == "[": #start list
            dictt_staff["start list"] = True
            dictt_staff["list"] = []
        
        elif letter == "T":
            dictt_staff["start true"] = True
        
        elif letter == "F":
            dictt_staff["start false"] = True
    #############################################
    #*----------if we started already----------*#
    #############################################
    #string
    elif dictt_staff["start str"]:
        if letter == "'": #if we need to end the string
            if dictt_staff["key"]: #if it a key
                dictt[dictt_staff["str"]] = ""
                dictt_staff["what_key"] = dictt_staff["str"]
                dictt_staff["key"] = False
                dictt_staff["str"] = ""
                dictt_staff["start str"] = False
            else: #if it a value
                dictt[dictt_staff["what_key"]] = dictt_staff["str"]
                dictt_staff["key"] = True
                dictt_staff["str"] = ""
                dictt_staff["start str"] = False
        else: #if we dont have to end the string
            dictt_staff["str"] += letter
    
    #integer
    elif dictt_staff["start int"]:
        if letter == ",": #if we need to end the int
            dictt[dictt_staff["what_key"]] = int(integer)
            dictt_staff["key"] = True
            dictt_staff["int"] = 0
            dictt_staff["start int"] = False
        else: #if we dont have to end the int
            dictt_staff["int"] += letter
    

    elif dictt_staff["start list"] and not start_list:
        if listttttt_for_staff(letter):
            pass
        else:
            dictt[dictt_staff["what_key"]] = listt
            dictt_staff["key"] = True
            listt = []
            listt_staff = {
                "int": 0,
                "str": "",
                "dict": {},
                "start int": False,
                "start str": False,
                "start dict": False,
                "start true": False,
                "start false": False
            }
            dictt_staff["start list"] = False

    elif dictt_staff["start true"]:
        if letter == "e":
            dictt[dictt_staff["what_key"]] = True
            dictt_staff["key"] = True
            dictt_staff["start true"] = False
    
    elif dictt_staff["start false"]:
        if letter == "e":
            dictt[dictt_staff["what_key"]] = False
            dictt_staff["key"] = True
            dictt_staff["start false"] = False
    
    else:
        if key:
            dictt[None] = ""
        else:
            dictt[dictt_staff["what_key"]] = None
    
    return True


def from_string_to_dict(dict_in_string):
    global the_final_dict, start_string, start_int, start_dict, start_list, start_true, start_false, key, string, listt, dictt, integer, what_key, dictt_staff, listt_staff

    dict_in_string_1 = dict_in_string[:-1]
    dict_in_string_for = dict_in_string_1[1:]
    start_string = False
    start_int = False
    start_dict = False
    start_list = False
    start_true = False
    start_false = False
    key = True
    string = ""
    listt = []
    dictt = {}
    integer = 0
    what_key = ""
    dictt_staff = {
        "key": True,
        "what_key": "",
        "int": 0,
        "str": "",
        "list": [],
        "start int": False,
        "start str": False,
        "start list": False,
        "start dict": False,
        "start true": False,
        "start false": False
        }
    listt_staff = {
        "int": 0,
        "str": "",
        "dict": {},
        "start int": False,
        "start str": False,
        "start dict": False,
        "start true": False,
        "start false": False
    }

    #######################################################################################################
    #*-----------------------------------------------start-----------------------------------------------*#
    #######################################################################################################
    for letter in dict_in_string_for:
        
        #if we need to start something
        if not start_string and not start_int and not start_dict and not start_list and not start_true and not start_false:

            if letter == "'": #start string
                start_string = True
            
            elif letter.isdigit(): #start int
                start_int = True
                integer = letter
            
            elif letter == "{": #start dict
                start_dict = True
                dictt = {}
            
            elif letter == "[": #start list
                start_list = True
                listt = []
            
            elif letter == "T":
                start_true = True
            
            elif letter == "F":
                start_false = True

        #############################################
        #*----------if we started already----------*#
        #############################################
        #string
        elif start_string:
            if letter == "'": #if we need to end the string
                if key: #if it a key
                    the_final_dict[string] = ""
                    what_key = string
                    key = False
                    string = ""
                    start_string = False
                else: #if it a value
                    the_final_dict[what_key] = string
                    key = True
                    string = ""
                    start_string = False
            else: #if we dont have to end the string
                string += letter
        
        #integer
        elif start_int:
            if letter == ",": #if we need to end the int
                the_final_dict[what_key] = int(integer)
                key = True
                integer = 0
                start_int = False
            else: #if we dont have to end the int
                integer += letter
        
        elif start_dict:
            if dictttttt_for_staff(letter):
                pass
            else:
                start_dict = False
                the_final_dict[what_key] = dictt
                key = True
                dictt = {}
                dictt_staff = {
                    "key": True,
                    "what_key": "",
                    "int": 0,
                    "str": "",
                    "list": [],
                    "start int": False,
                    "start str": False,
                    "start list": False,
                    "start dict": False,
                    "start true": False,
                    "start false": False
                }


        elif start_list:
            if listttttt_for_staff(letter):
                pass
            else:
                start_list = False
                the_final_dict[what_key] = listt
                key = True
                listt = []
                listt_staff = {
                    "int": 0,
                    "str": "",
                    "dict": {},
                    "start int": False,
                    "start str": False,
                    "start dict": False,
                    "start true": False,
                    "start false": False
                }


        elif start_true:
            if letter == "e":
                the_final_dict[what_key] = True
                key = True
                start_true = False
        
        elif start_false:
            if letter == "e":
                the_final_dict[what_key] = False
                key = True
                start_false = False

        
        else:
            if key:
                the_final_dict[None] = ""
            else:
                the_final_dict[what_key] = None

    #######################################################################
    #############################end of loop###############################
    #######################################################################


    #for the end
    if letter.isdigit():
        the_final_dict[what_key] = int(integer)
    
    
    #*-------------------------------return-------------------------------*#
    return the_final_dict

