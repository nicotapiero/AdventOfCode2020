count = 0

size = 35
from collections import defaultdict
memory = defaultdict(set)

# def parse_mask(s):
#     for i, char in enumerate(s):
#         if char == 1
#         32 - i

def write_helper(addr, curr_mask):
    blank = 0

    for i, char in enumerate(curr_mask):

        if char == '1':
            blank |= (1 << (size - i))
            111010
        elif char == '0':
            if addr >> (size-i) & 1:
                blank |= (1 << (size - i))
            # blank |= (addr & (2**size-1 & 0 << (size-i)))

    print(blank)

    possible_masks = [blank]

    if curr_mask.find('X') == -1:
        return possible_masks

    for i, char in enumerate(curr_mask):
        if char == 'X':
            copy = possible_masks.copy()
            for j, val in enumerate(copy):
                copy[j] = val | (1 << (size - i))
            print(copy)
            possible_masks.extend(copy)

    return possible_masks

# print(write_helper(42, '000000000000000000000000000000X1001X'))
# raise KeyError()


def write(start, mask):


    for i, char in enumerate(mask):
        # print(i)
        if char == '0':
            # print((1 << (size - i)))
            # memory[index] = memory[index]
            # print(memory[index], size-i, 'fuck', (2**36-1 ^ 1 << (size - i)))
            start &= (2**36-1 ^ 1 << (size - i))
        if char == '1':
            start |= (1 << (size - i))

    return start

    # print('write', memory[index])


with open('input.txt', 'r') as f:
    l = []
    lines = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.split('\n')

    
    lines = f.readlines()

    # print(lines)


    # new = []
    # print(lines[0][-1] == '\n')


    curr_mask = None
    for line in lines:

        if line.startswith('mask'):
            splits = line.split(' = ')
            mask = splits[1]
            # print(mask, splits[1])
            print(len(mask))
            curr_mask = mask
        else:
            splits = line.split(' = ')
            addr = int(splits[0][4:splits[0].find(']')])
            num = int(splits[1])
            print(addr, num)
            # if addr > len(memory):
            #     print(addr)
            #     raise KeyError()
            # memory[addr] = num
            masks = write_helper(addr, curr_mask)
            print('masks',masks)
            for mask in masks:
                memory[mask] = num
        print(memory)

    for key in memory:
        if memory[key]:
            count += memory[key]

    print('Count:', count)

    print(memory[8], memory[7])

#