count = 0


def parser(s):
    hexs = []
    cont = False
    for i, char in enumerate(s):
        if cont:
            cont = False
            continue
        if char in ['n', 's']:
            hexs.append(s[i:i+2])
            cont = True
        else:
            hexs.append(char)
    return hexs


# print(parser('nwwsweenw'))
from collections import defaultdict

class HexTile:
    def __init__(self):
        self.color = 'White'
        self.neighbors = dict()
        self.parent = None

    def create_new_tile(self, direction):
        new_hex = HexTile()
        self.neighbors[direction] = new_hex
        opposites = {'w':'e', 'e':'w', 'sw':'ne', 'se':'nw', 'nw':'se', 'ne':'sw'}
        new_hex.neighbors[opposites[direction]] = self
        new_hex.parent = self
        bfs_connect_neighbors(self, new_hex)


    def flip_color(self):
        if self.color == 'Black':
            self.color = 'White'
        else:
            self.color = 'Black'

def hex_bfs(reference_tile):
    print(reference_tile)
    seen = {reference_tile}
    queue = [reference_tile]

    count_black = 0
    while queue:
        curr = queue.pop(0)
        print(curr)
        if curr.color == 'Black':
            count_black += 1

        for _, neighbor in curr.neighbors.items():
            print('neighbor', neighbor)
            if neighbor not in seen:
                queue.append(neighbor)
                seen.add(neighbor)

    return count_black

def bfs_connect_neighbors(reference_tile, new_tile):
    queue = [reference_tile]
    seen = {reference_tile}

    layer1 = None
    layer2 = None
    layer0 = None

    previous_layer = None

    while queue:
        layer_len = len(queue)
        next_layer = {}
        for _ in range(layer_len):
            curr = queue.pop(0)

            for direction, neighbor in curr.neighbors.items():
                if neighbor not in seen:
                    next_layer[direction] = neighbor
                    queue.append(neighbor)
                    seen.add(neighbor)

        if new_tile in next_layer.values():
            layer1 = next_layer
            layer0 = previous_layer
        elif layer1 and not layer2:
            layer2 = next_layer
        else:
            previous_layer = next_layer



    # connect crap

    neighbors_layer1 = {'e' : ('ne', 'se'), 'ne' : ('e', 'nw'), 'se' : ('e', 'sw'),
                        'sw' : ('w', 'se'), 'w' : ('sw', 'nw'), 'nw' : ('w', 'ne')}

    print(layer1, layer2, layer0, reference_tile, new_tile)





with open('input.txt', 'r') as f:
    l = []

    lines = '''nwwswee'''.split('\n')

    # lines = f.readlines() # comment out this line to run above test case
    #
    # lines = [line[:-1] if line[-1] == '\n' else line for line in lines]

    reference_tile = HexTile()
    # for direction in ['w', 'e', 'sw', 'se', 'nw', 'ne']:
    #     reference_tile.neighbors[direction] = HexTile()

    # reference_tile.neighbors['nw'].neighbors['e'] = reference_tile.neighbors['ne']
    # reference_tile.neighbors['nw'].neighbors['sw'] = reference_tile.neighbors['w']
    #
    # reference_tile.neighbors['ne'].neighbors['w'] = reference_tile.neighbors['nw']
    # reference_tile.neighbors['ne'].neighbors['se'] = reference_tile.neighbors['e']
    #
    # reference_tile.neighbors['e'].neighbors['e'] = reference_tile.neighbors['ne']
    # reference_tile.neighbors['nw'].neighbors['e'] = reference_tile.neighbors['ne']
    #
    # reference_tile.neighbors['nw'].neighbors['e'] = reference_tile.neighbors['ne']
    # reference_tile.neighbors['nw'].neighbors['e'] = reference_tile.neighbors['ne']
    #
    # reference_tile.neighbors['nw'].neighbors['e'] = reference_tile.neighbors['ne']
    # reference_tile.neighbors['nw'].neighbors['e'] = reference_tile.neighbors['ne']
    #
    # reference_tile.neighbors['nw'].neighbors['e'] = reference_tile.neighbors['ne']
    # reference_tile.neighbors['nw'].neighbors['e'] = reference_tile.neighbors['ne']

    reference_tile.create_new_tile('se')
    raise KeyError()
    print(lines)

    for line in lines:
        curr = reference_tile
        for direction in parser(line):
            if direction not in curr.neighbors:
                curr.create_new_tile(direction)
            curr = curr.neighbors[direction]
            curr.flip_color()

    print(reference_tile)
    print('answer', hex_bfs(reference_tile))




    print('Count:', count)

# List of Wrong Answers:
#