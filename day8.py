count = 0

def decode(s):

    splits = s.split(' ')
    # print(s, splits)
    return (splits[0], int(splits[1]))

def check_loop(lines):
    pc = 0
    acc = 0
    visited = set()

    while pc < len(lines):
        print(pc, 'pc')
        # print(pc)
        visited.add(pc)
        decoded = lines[pc]
        # decoded = decode(lines[pc])
        if decoded[0] == 'nop':
            pc += 1
        elif decoded[0] == 'acc':
            acc += decoded[1]
            pc += 1
        elif decoded[0] == 'jmp':
            pc += decoded[1]
        else:
            raise KeyError()
        print(visited)
        if pc in visited:
            return -1
    return acc


with open('input.txt', 'r') as f:
    l = []
    lines = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split('\n')
    
    lines = f.readlines()

    lines = [decode(line) for line in lines]

    visited = set()

    for i, line in enumerate(lines):
        print(i)
        if line[0] == 'nop':
            copy = lines.copy()
            copy[i] = ('jmp', copy[i][1])

            ret = check_loop(copy)
            if  ret > -1:
                print('RETU',ret)
                break
        if line[0] == 'jmp':
            print(i, line)
            copy = lines.copy()
            copy[i] = ('nop', copy[i][1])
            print(copy)

            ret = check_loop(copy)
            print(ret, 'fuck')
            if ret > -1:
                print('RETU',ret)
                break

    # print('Count:', count)
