def pid_check(s):
    if len([letter for letter in s if letter.isdigit()]) != 9:
        return False

    return True

def hgt_check(s):
    if s[-2:] == 'cm':
        hgt = int(s[:-2])
        return 150 <= hgt <= 193
    elif s[-2:] == 'in':
        hgt = int(s[:-2])
        return 59 <= hgt <= 76
    else:
        return False

def iyr_check(s):
    if len(s) != 4:
        return False
    try:
        if not (2010 <= int(s) <= 2020):
            return False
    except:
        return False
    return True

def ecl_check(s):
    return s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def byr_check(s):
    if len(s) != 4:
        return False
    try:
        if not (1920 <= int(s) <= 2002):
            return False
    except:
        return False
    return True

def eyr_check(s):
    if len(s) != 4:
        return False

    try:
        if not (2020 <= int(s) <= 2030):
            return False
    except:
        return False
    return True

def hcl_check(s):
    if s[0] != '#':
        return False
    color = s[1:]
    digits = [letter for letter in color if letter.isdigit() or letter in 'abcdef']
    if len(digits) != 6:
        return False
    return True

def cid_check(s):
    return True

d = {'pid:': pid_check, 'byr:': byr_check,'iyr:': iyr_check,
     'hcl:': hcl_check,'hgt:': hgt_check,'eyr:': eyr_check,
     'ecl:': ecl_check, 'cid:':cid_check}

with open("input.txt", "r") as f:
#     passports = '''eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
#
# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946
#
# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
#
# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007'''.split('\n\n')

    passports = f.read().split('\n\n')
    count = 0
    for passport in passports:
        if passport.find('ecl:') > -1 and passport.find('pid:') > -1 \
            and passport.find('byr:') > -1 and passport.find('iyr:') > -1 \
                and passport.find('hgt:') > -1 and passport.find('hcl:') > -1 \
                and passport.find('eyr:') > -1:
            reject = False
            for field in passport.split():
                code = field[:4]
                rest = field[4:]

                print(code, rest)
                if not d[code](rest):
                    reject= True

            print('\n')
            if not reject:
                count += 1
    print(count)