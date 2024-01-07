count = 0

from collections import defaultdict

def get_quantifiers(s):
    return s.strip().split(' ')[:3]

def bfs(d, key, find):
    seen = set()

    queue = [key]


    while queue:

        curr = queue.pop(0)
        seen.add(curr)
        if curr == find:
            return True
        if curr in d:
            for neighbor in d[curr]:
                if neighbor not in seen:
                    queue.append(neighbor)


    return False

def bfs2(d, key):
    seen = set()

    queue = [(key, 1)]
    count = -1
    parent = {key : None}
    multiplier = {key : 1}

    while queue:
        curr, quant = queue.pop(0)
        quant= int(quant)
        print(curr, multiplier, quant)
        print(queue)
        if curr not in seen:
            seen.add(curr)

        else:
            continue

        if curr in d:
            count += multiplier[curr]
            for neighbor in d[curr]:
                print(neighbor)
                if neighbor[0] not in seen:
                    queue.append(neighbor)
                    parent[neighbor[0]] = curr
                    multiplier[neighbor[0]] = multiplier[curr] * int(neighbor[1])

        else:
            print(curr, multiplier[curr], multiplier[parent[curr]], quant)
            count += quant * multiplier[parent[curr]]
        print('cournt', count)

    return count

with open('input.txt', 'r') as f:
    l = []
    lines = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''.split('\n')
    d = defaultdict(set)
    
    # lines = f.readlines()

    for line in lines:
        if line.find(' contain no other bags.') > 0:
            continue
        splits = line.split(',')
        # print(splits)
        i1, i2 = splits[0].split(' contain ')
        splits = splits[1:]

        i1 = i1[:i1.find(' bags')]
        quant, adj, color = get_quantifiers(i2)
        d[i1].add((adj + ' ' + color, quant))
        if splits:
            for split in splits:
                # print(split)
                # print(get_quantifiers(split))
                quant, adj, color = get_quantifiers(split)
                d[i1].add((adj + ' ' + color, quant))

    print('bfs')
    og_keys = d.keys()
    d = dict(d)
    # for key in d:
    print(d)
    print(bfs2(d, 'shiny gold'), 'ands')

# 170 nope

    print('Count:', count)

# 3193 nope
# 2292
# 2232