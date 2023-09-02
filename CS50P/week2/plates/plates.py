def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_start(s):
        if check_lenght(s):
            if check_number(s):
                if check_spaces(s):
                    return True
    return False

def check_start(s):
    for i in range(min(len(s),2)):
        if s[i].isdigit():
            #print("Fail 1")
            return False
    return True

def check_lenght(s):
    if 1 < len(s) < 7:
        return True
    else:
        #print("Fail 2")
        return False

def check_number(s):
    if check_first_digit(s) and check_int_digit(s):
        return True
    else:
        return False

def check_spaces(s):
    for i in range(len(s)):
        if not (s[i].isalnum()):
            #print("Fail 5")
            return False
    return True

def check_first_digit(s):
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                #print("Fail 3")
                return False
            else:
                return True
    return True
def check_int_digit(s):
    for i in range(len(s)-1):
        if s[len(s)-i-1].isalpha():
            if s[len(s)-i-2].isdigit():
                #print("Fail 4")
                return False
    return True

main()