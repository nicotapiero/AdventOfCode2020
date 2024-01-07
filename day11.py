count = 0


with open('input.txt', 'r') as f:
    l = []
    lines = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.split('\n')

#     lines = '''16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4'''.split('\n')
    
    lines = f.readlines()

    print(lines)


    new = []
    print(lines[0][-1] == '\n')

    for line in lines:
        if line[-1] == '\n':
            new.append(line[:-1])
        else:
            new.append(line)
    lines= new

    old_lines = lines



    while True:
        copy = [line[:] for line in lines]

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                adj = 0
                options = [(i + 1, j + 1),
                           (i, j + 1),
                           (i, j - 1),
                           (i + 1, j - 1),
                           (i + 1, j),
                           (i - 1, j),
                           (i - 1, j - 1),
                           (i - 1, j + 1)]
                filtered = [(x, y) for x, y in options if 0 <= x < len(lines) and 0 <= y < len(line)]

                if char != '.':
                    occupied = 0
                    # for x, y in filtered:
                    #     if lines[x][y] == '#':
                    #         occupied += 1
                    x = i+1
                    while x < len(lines) and lines[x][j] == '.': x += 1
                    if x < len(lines):
                        if lines[x][j] == '#':
                            occupied +=1
                    x = i-1
                    while x >= 0 and lines[x][j] == '.': x -= 1
                    if x >= 0:
                        print(x, j, lines[x][j])
                        if lines[x][j] == '#':
                            occupied +=1
                    x = i
                    y = j+1
                    while y < len(line) and lines[i][y] == '.': y += 1
                    if y < len(line):
                        if lines[i][y] == '#':
                            occupied +=1
                    y = j-1
                    while y >= 0 and lines[i][y] == '.': y -= 1
                    if y >= 0:
                        if lines[i][y] == '#':
                            occupied += 1

                    x = i + 1
                    y = j + 1
                    while x < len(lines) and y < len(line) and lines[x][y] == '.' : y += 1; x+=1
                    if y < len(line) and x < len(line):
                        if lines[x][y] == '#':
                            occupied += 1

                    x = i - 1
                    y = j - 1
                    while x >= 0 and y >= 0 and lines[x][y] == '.': y -= 1; x -= 1
                    if y >= 0 and x >= 0:
                        if lines[x][y] == '#':
                            occupied += 1

                    x = i + 1
                    y = j - 1
                    while x < len(lines) and y >= 0 and lines[x][y] == '.': y -= 1; x += 1
                    if y >= 0 and x < len(lines):
                        if lines[x][y] == '#':
                            occupied += 1

                    x = i - 1
                    y = j + 1
                    while x >= 0 and y < len(line) and lines[x][y] == '.': y += 1; x -= 1
                    if y < len(line) and x >= 0:
                        if lines[x][y] == '#':
                            occupied += 1

                    if char == '#':
                        if occupied >= 5:
                            copy[i] = copy[i][:j] + 'L' + copy[i][j+1:]
                    if char == 'L':
                        if occupied == 0:
                            copy[i] = copy[i][:j] + '#' + copy[i][j + 1:]
                    print('occ', i, j, occupied)


                # if char == '#':
                #     occupied = 0
                #     for x, y in filtered:
                #         if lines[x][y] == '#':
                #             occupied += 1
                #     if occupied >= 5:
                #         copy[i] = copy[i][:j] + 'L' + copy[i][j+1:]
        print(filtered)
        print(options)
        lines = copy
        print(copy)
        same = True
        for line1, line2 in zip(lines, old_lines):
            if line1 != line2:
                same = False
        if same == True:
            break
        old_lines = lines

    print('fuck')
    print(lines)
    for line in lines:
        for char in line:
            print(line)
            if char == '#':
                count+=1
                print(count, char, )

    print('Count:', count)

#