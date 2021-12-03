"""
    Advent of Code 2020 Day 4
    --- Day 4: Passport Processing ---
            Glory to Arstotzka
    
"""

def partOne(passports, cid_r, validation):
    allowed_passports = 0
    valid_passports = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if(cid_r): required_fields.append("cid")
    
    for passport in passports:
        passport_split = passport.split("\n")
        this_passport_properties = []
        for line in passport_split:
            this_passport_properties.append(line.split(" "))
        
        this_passport = []
        if(len(this_passport_properties) > 1):
            for h in range(len(this_passport_properties)):
                this_passport += this_passport_properties[h]
        else:
            this_passport = this_passport_properties[0]
        index = 0
        for i in this_passport:
            this_passport[index] = i.split(":")
            index+=1
        
        req_fields = 0
        for j in this_passport:
            for k in required_fields:
                if j[0] == k: req_fields+=1
        if(cid_r):
            if req_fields >= 8: 
                allowed_passports+=1
                if(validateField(this_passport)):
                    valid_passports+=1
        else:
            if req_fields >= 7: 
                allowed_passports+=1
                if(validateField(this_passport)):
                    valid_passports+=1

    if(validation):
        return valid_passports
    return allowed_passports

def checkByr(b):
    b_int = int(b)
    return 1920 <= b_int and b_int <= 2002

def checkIyr(i):
    i_int = int(i)
    return 2020 >= i_int and i_int >= 2010

def checkEyr(e):
    e_int = int(e)
    return 2020 <= e_int and e_int <= 2030

def checkHgt(h):
    if(h[-2:] == "in"):
        return int(h[0:-2]) >= 59 and int(h[0:-2]) <= 76
    elif(h[-2:] == "cm"):
        return int(h[0:-2]) >= 150 and int(h[0:-2]) <= 193
    return False

def checkHcl(hcl):
    color = hcl[1:]
    if(hcl[0] != "#") or (len(color) != 6): return False

    allowed = "abcdef0123456789"
    for let in color:
        if not let in allowed:
            return False
    return True
def checkEcl(ecl):
    allowed = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in allowed

def checkPid(pid):
    return len(pid) == 9 and pid.isnumeric() 
def checkCid(c):
    return True

def validateField(pp):
    check_dir = {
        "byr": checkByr,
        "iyr": checkIyr,
        "eyr": checkEyr,
        "hgt": checkHgt,
        "hcl": checkHcl,
        "ecl": checkEcl,
        "pid": checkPid,
        "cid": checkCid
    }

    pp_valid = True
    for prop in pp:
        if pp_valid:
            pp_valid = check_dir[prop[0]](prop[1])
        else:
            return pp_valid
    return pp_valid


def main():
    with open("Hobbyprojekt/adventofcode/2020/inputdec04.txt", "r") as f:
        puzzle_input = [blocks for blocks in f.read().split("\n\n")]
    
    with open("Hobbyprojekt/adventofcode/2020/example04.txt", "r") as g:
        example_input = [blocks for blocks in g.read().split("\n\n")]
    
    """
        Example should return 1st valid, 2nd invalid, 3rd valid, 4th invalid
        2 valid, 2 invalid

        A password requires all fields, except cid.
        You may make cid optional.
        Return how many valid passwords there are.
    """

    print("Valid passports: ", partOne(example_input, True, False))
    print("Valid passports, cid optional: ", partOne(example_input, False, False))
    
    print("Valid passports: ", partOne(puzzle_input, True, False))
    #print 128
    print("Valid passports, cid optional: ", partOne(puzzle_input, False, False))
    #print 237
    #print("Extra validated example passports:", partOne(example_input, False, True))
    print("Extra validated passports:", partOne(puzzle_input, False, True))
    #print 172
main()