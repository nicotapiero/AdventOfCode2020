from collections import Counter

with open('input.txt', 'r') as f:
    lines = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''.split('\n')
    lines = f.readlines()
    count = 0
    for line in lines:
        # print(line)
        (range, letter, password) = line.split()
        counts = Counter(password)
        letter = letter[0]
        pos1, pos2 = int(range[:range.find('-')]), int(range[range.find('-')+1:])
        if True:
            # print(pos1, pos2)
            # print(password[pos1-1], password[pos2-1], letter)
            if password[pos1-1] == letter or password[pos2-1] == letter:
                print(password, password[pos1 - 1], password[pos2 - 1], pos1, pos2, letter, line)

            if password[pos1-1] != letter and password[pos2-1] != letter:
                print('case1', line)
                continue

            if password[pos1-1] == password[pos2-1] == letter:
                print('case2')
                continue
            # pos1
            # print('hah')
            count+=1

    print(count)

# 221 - too low
