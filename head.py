from random import randint
import sys, os, time
import datetime as dt
import webbrowser as wb
from colorama import *
from colorama import Fore
from abc import ABC, abstractmethod

args = sys.argv

TRUE = "1b"
FALSE = "0b"

PFIX_FUNC = "-"
PFIX_VAR = "$"
PFIX_CONST = "_"
PFIX_KWORD = "?"
PFIX_OBJ = "#"
PFIX_COM = "/"
PFIX_DECOR = "@"

SFIX_FUNC_FLUSH = "flush"
SFIX_FUNC_FLUSHYELLOW = "flush<color:warn>"
SFIX_FUNC_FLUSHRED = "flush<color:err>"
SFIX_FUNC_FLUSHDEBUG = "flushdb"
SFIX_FUNC_SYS = "sys"
SFIX_FUNC_WB = "web"
SFIX_FUNC_ERR = "err"
SFIX_FUNC_SQUARE = "square"
SFIX_FUNC_CUBE = "cube"
SFIX_FUNC_RANDOM_INTEGER = "ri"

SFIX_KWORD_INCLUDE = "include"
SFIX_KWORD_FUNC = "func"
SFIX_KWORD_IF = "if"
SFIX_KWORD_LOOP = "loop"

OP_KWORD_IF_EQUALS = "=="
OP_KWORD_IF_EQUALS_NOT = "!="

v_names = ["__debug__"]
v_values = ["01234567899876543210"]

c_names = ["f"]
c_values = ["xx7777"]

f_names = ["test"]
f_values = ["-flush This was a test!"]

im = []

suffix_head = ""
suffix_tail = ""
suffix_tail_sp = []

read_lock = False
is_end = False

def glue(data : list):
    out = ""
    for n in data:
        out = out + " " + n
    return out

class DefaultClass(ABC):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @abstractmethod
    def IDc(self, idc : str, args = []):
        pass

    def trier(self):
        print("Yipeee!")

class DebugClass(DefaultClass):
    def __init__(self):
        pass

    def IDc(self, idc : str, args = []):
        if idc == "-testmethod":
            self.testmethod()
        
    
    def testmethod(self):
        print("Working!")

class studioLT3_Studio(DefaultClass):
    def __init__(self):
        self.studio_v_names = []
        self.studio_v_values = []

        self.studio_c_names = []
        self.studio_c_values = []

        self.studio_f_names = []
        self.studio_f_values = []

    def IDc(self, idc : str, args = []):
        if idc == "-getall":
            self.getall()
        elif idc == "-var":
            self.assign_var(args[0], glue(args[1:]))
        elif idc == "-const":
            self.assign_const(args[0], glue(args[1:]))
        elif idc == "-func":
            self.assign_func(args[0], glue(args[1:]))

    def getall(self):
        print(f"Studio Values : vars[names[{self.studio_v_names}],values[{self.studio_v_values}]],constants[names[{self.studio_c_names}],values[{self.studio_c_values}]],funcs[names[{self.studio_f_names}],values[{self.studio_f_values}]]")
    
    def assign_var(self, name, value):
        self.studio_v_names.append(name)
        self.studio_v_values.append(value)

    def assign_const(self, name, value):
        self.studio_c_names.append(name)
        self.studio_c_values.append(value)
    
    def assign_func(self, name, value):
        self.studio_f_names.append(name)
        self.studio_f_values.append(value)

class math_Calculator(DefaultClass):
    def __init__(self):
        pass

    def IDc(self, idc : str, args = []):
        if idc == "-add":
            self.add(args)
    
    def add(self, args):
        out = 0
        for f in args:
            out = out + int(f)
        return f


# Created Objects
obj = {"__debugobject__":DebugClass()}
# Doggos <3

def format_string(string : str):
    for i in range(len(v_names)):
        actual_v_id = i
        actual_v_name = v_names[actual_v_id]
        actual_v_value = v_values[actual_v_id]
        if type(actual_v_value) == str:
            string = string.replace(PFIX_VAR + actual_v_name, actual_v_value)
    for i in range(len(c_names)):
        actual_c_id = i
        actual_c_name = c_names[actual_c_id]
        actual_c_value = c_values[actual_c_id]
        string = string.replace(PFIX_CONST + actual_c_name, actual_c_value)

    return string

def format_expressions(string : str):
    # <<ask>>
    if "<<ask>>" in string:
        string = string.replace("<<ask>>", input(" "))
    # [<<ri>>x2x3]
    #     |   | |
    #    ri  n1 n2
    if "[<<ri>>" in string:
        tempPOS1 = string.find("[<<ri>>")
        tempPOS2 = string.find("]")
        tempSTR = string[tempPOS1:tempPOS2+1]
        tempSTR = tempSTR.replace("[", "").replace("]", "")
        tempSTRSPLIT = tempSTR.split("x")
        tempA = int(tempSTRSPLIT[1])
        tempB = int(tempSTRSPLIT[2])
        string = string.replace(tempSTR, str(randint(tempA, tempB)))
        string = string.strip("[")
        string = string.strip("]")
        string = string.replace("[", "").replace("]", "")

    return string

def err(type : str, desc : str):
    return f"{Fore.RED}Error found:\n   <script>\n{type} : {desc}{Fore.RESET}"

def scissors(string : str):
    prefix = string[0]
    suffix = string[1:]
    return [prefix, suffix]

def glue(data : list):
    out = ""
    for n in data:
        out = out + " " + n
    return out

# Class Checker
def check_classes(id : str, name : str, args = []):
    if id == "__debugclass__":
        obj[name] = DebugClass()
        return None
    elif id == "Studio":
        obj[name] = studioLT3_Studio()
        return None
    else:
        return err("ClassError", f"Class \"{id}\" not found in the class registery.")

def check_if(iss : str) -> bool:
    isc = iss.split(" ")

    if len(isc) == 3:
        var1 = isc[0]
        check = isc[1]
        var2 = isc[2]

        var1 = format_string(var1)
        var2 = format_string(var2)

        if check == OP_KWORD_IF_EQUALS:
            if var1 == var2:
                return True
            else:
                return False
        elif check == OP_KWORD_IF_EQUALS_NOT:
            if not var1 == var2:
                return True
            else:
                return False
        else:
            return err("OperatorError", f"Invalid operator : {check}.")

def im_math():
    im.append("math")

    c_names.append("pi")
    c_values.append("3.14")

    obj["calculator"] = math_Calculator()

def im_web():
    im.append("web")

def im_studioLT3():
    im.append("studioLT3")

    v_names.append("currentStudio")
    v_values.append("__head__")
    v_names.append("currentStudioBp")
    v_values.append("__head__bp")

    f_names.append("studioFlush")
    f_values.append("-flush <$currentStudio - breakpoint set to $currentStudioBp>")

    f_names.append("currentStudioErrShouting")
    f_values.append("-err studioLT3.studioError Studio shouted this error.")

    obj["__defaultStudio__"] = studioLT3_Studio()

def im_random():
    im.append("random")

def classify(data : list) -> str:
    global read_lock

    prefix = data[0]
    suffix = data[1]

    suffix_sp = suffix.split(" ")
    suffix_tail_sp = suffix_sp[1:]

    suffix_head = suffix_sp[0]
    if not len(suffix_sp) == 1:
        temp = suffix.find(" ")+1
        suffix_tail = suffix[temp:]
    else:
        suffix_tail = suffix_tail_sp

    if read_lock == False:
            if len(data) == 2:

                if prefix == PFIX_FUNC:
                    if suffix_head == SFIX_FUNC_FLUSH:
                        if not len(suffix_sp) == 1:
                            temp2 = suffix_tail
                            temp2 = format_string(temp2)
                            return temp2
                        else:
                            return err("ArgumentError", "Needed argument is missing.")
                    elif suffix_head == SFIX_FUNC_FLUSHYELLOW:
                        if not len(suffix_sp) == 1:
                            temp2 = suffix_tail
                            temp2 = format_string(temp2)
                            return f"{Fore.YELLOW}{temp2}{Fore.RESET}"
                        else:
                            return err("ArgumentError", "Needed argument is missing.")
                    elif suffix_head == SFIX_FUNC_FLUSHRED:
                        if not len(suffix_sp) == 1:
                            temp2 = suffix_tail
                            temp2 = format_string(temp2)
                            return f"{Fore.RED}{temp2}{Fore.RESET}"
                        else:
                            return err("ArgumentError", "Needed argument is missing.")
                    elif suffix_head == SFIX_FUNC_FLUSHDEBUG:
                        return f"{Fore.CYAN}This is a debug message. Have a great day!{Fore.RESET}"
                    elif suffix_head == SFIX_FUNC_SYS:
                        try:
                            os.system(suffix_tail)
                        except:
                            return err("SysError", "Unknown SYS cl error.")
                    elif suffix_head == SFIX_FUNC_ERR:
                        return err(suffix_tail_sp[0], suffix_tail.replace(suffix_tail_sp[0] + " ", ""))

                    # DEFINED FUNCTIONS

                    for i in range(len(f_names)):
                        actual_f_id = i
                        actual_f_name = f_names[actual_f_id]
                        actual_f_value = f_values[actual_f_id]

                        if suffix_head == actual_f_name:
                            return classify(scissors(actual_f_value.replace(actual_f_name + " ", "")))

                    # ADDITIONAL FUNCTIONS (AVAILABLE ONLY THROUGH ?include INSTRUCTIONSD)

                    if "web" in im:
                        if suffix_head == SFIX_FUNC_WB:
                            try:
                                wb.open(suffix_tail)
                            except:
                                return err("WebOpeningError", "Unknown WEBOPENINGS error.")
                    if "math" in im:
                        if suffix_head == SFIX_FUNC_SQUARE:
                            return str(int(suffix_tail_sp[0]) * int(suffix_tail_sp[0]))
                        if suffix_head == SFIX_FUNC_CUBE:
                            return str(int(suffix_tail_sp[0]) * int(suffix_tail_sp[0]) * int(suffix_tail_sp[0]))
                    if "random" in im:
                        if suffix_head == SFIX_FUNC_RANDOM_INTEGER:
                            return format_expressions(f"[<<ri>>x{suffix_tail_sp[0]}x{suffix_tail_sp[1]}]")
                elif prefix == PFIX_VAR:
                    if not len(suffix_tail_sp) == 0:
                        if suffix_tail_sp[0] == "=":
                            if not suffix_tail.replace("= ", "").startswith(PFIX_FUNC):
                                if not suffix_head in v_names:
                                    v_names.append(suffix_head)
                                    v_values.append(suffix_tail.replace("= ", ""))
                                else:
                                    v_values[v_names.index(suffix_head)] = suffix_tail.replace("= ", "")
                            else:
                                if not suffix_head in v_names:
                                    v_names.append(suffix_head)
                                    v_values.append(classify(scissors(suffix_tail.replace("= ", ""))))
                                else:
                                    v_values[v_names.index(suffix_head)] = classify(scissors(suffix_tail.replace("= ", "")))
                    else:
                        return err("ArgumentError", "Needed argument is missing.")
                elif prefix == PFIX_CONST:
                    if not len(suffix_tail_sp) == 0:
                        if suffix_tail_sp[0] == "=":
                            if not suffix_tail.replace("= ", "").startswith(PFIX_FUNC):
                                if not suffix_head in c_names:
                                    c_names.append(suffix_head)
                                    c_values.append(suffix_tail.replace("= ", ""))
                                else:
                                    return err("ImmutableObjectModificationError", "Cannot modify <CONST> data type.")
                            else:
                                if not suffix_head in v_names:
                                    v_names.append(suffix_head)
                                    v_values.append(classify(scissors(suffix_tail.replace("= ", ""))))
                                else:
                                    return err("ImmutableObjectModificationError", "Cannot modify <CONST> data type.")
                    else:
                        return err("ArgumentError", "Needed argument is missing.")
                elif prefix == PFIX_KWORD:
                    if not len(suffix_tail_sp) == 0:
                        if suffix_head == SFIX_KWORD_INCLUDE:
                            if suffix_tail_sp[0] == "math":
                                im_math()
                            elif suffix_tail_sp[0] == "web":
                                im_web()
                            elif suffix_tail_sp[0] == "studioLT3":
                                im_studioLT3()
                            elif suffix_tail_sp[0] == "random":
                                im_random()
                            else:
                                if f"{suffix_tail_sp[0]}.sp" in os.listdir("packages\\external"):
                                    run_file(f"packages\\external\\{suffix_tail_sp[0]}.sp")
                                else:
                                    return err("IncludeModuleError", f"Module \"{suffix_tail_sp[0]}\" not found.")
                        elif suffix_head == SFIX_KWORD_FUNC:
                            if suffix_tail_sp[1] == "=":
                                if not suffix_head in f_names:
                                    f_names.append(suffix_tail_sp[0])
                                    f_values.append(suffix_tail.replace("= ", ""))
                                else:
                                    return err("ImmutableObjectModificationError", "Cannot modify <FUNC> data type.")
                            else:
                                return err("MarkError", "Expected \"=\" mark.")
                        elif suffix_head == SFIX_KWORD_IF:
                            if check_if(suffix_tail.replace(" {", "")):
                                pass
                            else:
                                read_lock = True
                        elif suffix_head == SFIX_KWORD_LOOP:
                            pass
                    else:
                        return err("ArgumentError", "Needed argument is missing.")
                elif prefix == PFIX_OBJ:
                    if suffix_tail_sp[0] == ".":
                        if suffix_head in obj:
                            obj[suffix_head].IDc(suffix_tail_sp[1].replace(". ", ""), suffix_tail_sp[1:])
                    elif suffix_tail_sp[0] == "=":
                        check_classes(suffix_tail_sp[1], suffix_head, suffix_tail_sp[2:])
                elif prefix == PFIX_COM:
                    pass
                elif prefix == PFIX_DECOR:
                    if suffix_head == "silent":
                        return ["@silent", classify(scissors(suffix_tail))]
                elif prefix == "}":
                    pass
                else:
                    return err("PrefixError", "Invalid prefix.")
            else:
                return err("BuiltinListError", "Error in built-in list.")
    else:
        if prefix == "}":
            read_lock = False
    
    if prefix == "}":
        cur_repeats = 1

def run_file(pathin):
    global is_end, end_stamp
    if os.path.exists(pathin):
        file = open(pathin, "r")
        data = file.readlines()
        for r in data:
            r = format_expressions(r)
            temp420 = classify(scissors(r.strip("\n")))
            if not temp420 == None:
                print(temp420)
        is_end = True
        end_stamp = time.time()
        temp3110 = round(end_stamp - run_stamp, 2)
        if temp3110 >= 0.3:
            print(f"\n{Fore.LIGHTGREEN_EX}[RUN]{Fore.RESET} Runtime finished in {temp3110} seconds.\n")
        else:
            print(f"\n{Fore.LIGHTGREEN_EX}[RUN]{Fore.RESET} Runtime finished in ~ 0.2 seconds.\n")

if len(args) == 1:
    while True:
        temp69 = input(f"{Fore.LIGHTYELLOW_EX}> {Fore.RESET}")
        temp69 = format_expressions(temp69)
        temp2307 = classify(scissors(temp69))
        if not type(temp2307) == list:
            if not temp2307 == None:
                print(temp2307)
        else:
            if not temp2307[0] == "@silent":
                if not temp2307 == None:
                    print(temp2307)
else:
    run_stamp = time.time()
    is_end = False
    run_file(args[1])
