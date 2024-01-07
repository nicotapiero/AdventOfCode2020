count = 0

def get_blank(lines):
    l = []
    for _ in lines:
        l.append('.'* len(lines[0]))
    # print(l)
    return l

def get_neighbors(lines, z_out, i, j):
    # print(lines,'fuck', len(lines), len(lines[0]), len(lines[0][0]))
    l = []
    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            for dz in range(-1, 2, 1):
                if dx == dy == dz == 0:
                    continue
                x, y, z = i - dx, j-dy, z_out-dz

                try:
                    lines[z][x][y]
                    l.append((x, y, z))
                except:
                    continue

                # if -len(lines)//2 <= z <= len(lines)//2 and 0 <= x < len(lines[0]) and 0 <= y < len(lines[0][0]):
                #     l.append((x, y, z))
    # print(l)
    return l

def extend(s, l,n):
    return l*n + s + l*n

num_iterations = 3

with open('input.txt', 'r') as f:
    l = []
    lines = '''.#.
..#
###'''.split('\n')

    # lines = f.readlines()

    # print(lines)

    lines = [extend(line, '.', num_iterations) for line in lines]

    l = [lines]
    for _ in range(num_iterations*2):
        l.append(get_blank(lines))

    lines = l

    for layer in lines:
        for _ in range(num_iterations):
            layer.insert(0, '.'* len(layer[0]))
        for _ in range(num_iterations):
            layer.append('.' * len(layer[0]))



    # print(l)



    print(len(get_neighbors(lines, 0, 1, 1)))
    # raise KeyError

    old_lines = [la[:] for la in lines]

    # print(old_lines)

    for _ in range(num_iterations):
        for layer in range(-len(lines)//2, len(lines)//2+1, 1):
            for i, string in enumerate(lines[layer]):
                for j, char in enumerate(string):
                    print(layer, i, j)
                    if layer == 0 and i == 3 and j == 2:
                        print(layer, i, j)
                        print('fuck')
                        print(get_neighbors(lines, layer, i, j))

                    num_active = 0
                    for (neighbor_i, neighbor_j, neighbor_z) in get_neighbors(lines, layer, i, j):
                        # print(len(lines), len(lines[0]), len(lines[0][0]), neighbor_i, neighbor_j, neighbor_z)
                        if lines[neighbor_z][neighbor_i][neighbor_j] == '#':
                            num_active += 1

                    print(num_active)
                    if lines[layer][i][j] == '#':
                        if num_active != 2 and num_active != 3:
                            old_lines[layer][i] = old_lines[layer][i][:j] + '.' + old_lines[layer][i][j+1:]
                        else:
                            old_lines[layer][i] = old_lines[layer][i][:j] + '#' + old_lines[layer][i][j + 1:]
                    else:
                        if num_active == 3:
                            print(num_active)
                            old_lines[layer][i] = old_lines[layer][i][:j] + '#' + old_lines[layer][i][j+1:]
                        else:
                            old_lines[layer][i] = old_lines[layer][i][:j] + '.' + old_lines[layer][i][j + 1:]

        print(old_lines, lines, 'fuq')

        lines = old_lines
        old_lines = [l[:] for l in lines]

    for layer in range(-2, 3, 1):
        for i, string in enumerate(lines[layer]):
            for j, char in enumerate(string):
                if char == '#':
                    count += 1



    print('Count:', count)


# 98