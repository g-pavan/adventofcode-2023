def first_value_finder(string):

    for i in range(len(string)):
        if (string[i] == "1") or (string[i] == "o" and len(string) > i+2 and string[i:i+3] == "one"):
        # if (string[i] == "1"):
            return "1"

        if (string[i] == "2") or (string[i] == "t" and len(string) > i+2 and string[i:i+3] == "two"):
        # if (string[i] == "2"):
            return "2"
        
        if (string[i] == "3") or (string[i] == "t" and len(string) > i+2 and string[i:i+3] == "two"):
        # if (string[i] == "3"):
            return "3"

        if (string[i] == "4") or (string[i] == "f" and len(string) > i+4 and string[i:i+5] == "three"):
        # if (string[i] == "4"):
            return "4"
        
        if (string[i] == "5") or (string[i] == "f" and len(string) > i+3 and string[i:i+4] == "five"):
        # if (string[i] == "5"):
            return "5"
        
        if (string[i] == "6") or (string[i] == "s" and len(string) > i+2 and string[i:i+3] == "six"):
        # if (string[i] == "6"):
            return "6"
        
        if (string[i] == "7") or (string[i] == "s" and len(string) > i+4 and string[i:i+5] == "seven"):
        # if (string[i] == "7"):
            return "7"

        if (string[i] == "8") or (string[i] == "e" and len(string) > i+4 and string[i:i+5] == "eight"):
        # if (string[i] == "8"):
            return "8"
        
        if (string[i] == "9") or (string[i] == "n" and len(string) > i+3 and string[i:i+4] == "nine"):
        # if (string[i] == "9"):
            return "9"
    
    return "0"

def second_value_finder(string):

    for i in range(len(string)-1, -1, -1):
        if (string[i] == "1") or (string[i] == "o" and len(string) > i+2 and string[i:i+3] == "one"):
        # if (string[i] == "1"):
            return "1"

        if (string[i] == "2") or (string[i] == "t" and len(string) > i+2 and string[i:i+3] == "two"):
        # if (string[i] == "2"):
            return "2"
        
        if (string[i] == "3") or (string[i] == "t" and len(string) > i+2 and string[i:i+3] == "two"):
        # if (string[i] == "3"):
            return "3"

        if (string[i] == "4") or (string[i] == "f" and len(string) > i+4 and string[i:i+5] == "three"):
        # if (string[i] == "4"):
            return "4"
        
        if (string[i] == "5") or (string[i] == "f" and len(string) > i+3 and string[i:i+4] == "five"):
        # if (string[i] == "5"):
            return "5"
        
        if (string[i] == "6") or (string[i] == "s" and len(string) > i+2 and string[i:i+3] == "six"):
        # if (string[i] == "6"):
            return "6"
        
        if (string[i] == "7") or (string[i] == "s" and len(string) > i+4 and string[i:i+5] == "seven"):
        # if (string[i] == "7"):
            return "7"

        if (string[i] == "8") or (string[i] == "e" and len(string) > i+4 and string[i:i+5] == "eight"):
        # if (string[i] == "8"):
            return "8"
        
        if (string[i] == "9") or (string[i] == "n" and len(string) > i+3 and string[i:i+4] == "nine"):
        # if (string[i] == "9"):
            return "9"
    
    return "0"

def calibration_value(string):

    first_value = first_value_finder(string)
    second_value = second_value_finder(string)

    # print(f"string: {string} has first value: {first_value} second value: {second_value}")

    return int(first_value+second_value)


if __name__ ==  "__main__":

    ans = 0

    with open("input.txt", "r") as f:
        for line in f:
            ans += calibration_value(line.strip())
    
    print(ans)