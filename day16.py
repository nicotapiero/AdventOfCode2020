count = 0

def parse_first(s):
    d = {}
    for line in s.split('\n'):
        (feature, nums) = line.split(': ')
        range1, range2 = nums.split(' or ')
        range1, range2 = range1.split('-'), range2.split('-')
        range1, range2 = (int(range1[0]), int(range1[1])), (int(range2[0]), int(range2[1]))
        d[feature] = (range1, range2)
    print(d)
    return d

def parse_ticket(s):
    _, numbers = s.split('\n')
    l = numbers.split(',')
    l = [int(i) for i in l]
    print('ell,', l)
    return l

def parse_nearby(s):
    l = []
    for line in s.split('\n')[1:]:
        nums = line.split(',')
        nums = [int(num) for num in nums]
        l.append(nums)
    return l

with open('input.txt', 'r') as f:
    l = []
    lines = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''.split('\n\n')

    lines = f.read().split('\n\n')

    d = parse_first(lines[0])
    ticket = parse_ticket(lines[1])
    nearby_tickets = parse_nearby(lines[2])

    


    ages = {}

    good = []
    idx = []
    count = []
    for i, nearby_ticket in enumerate(nearby_tickets):
        if i == 218:
            print('oh oh')
        # print('nbt',nearby_ticket)
        old_count = count.copy()
        for item in nearby_ticket:
            is_bad = True
            for range1, range2 in d.values():
                if range1[0] <= item <= range1[1]:
                    is_bad = False
                if range2[0] <= item <= range2[1]:
                    is_bad = False

            if is_bad:
                print(nearby_ticket, item)
                count.append(item)

        if count == old_count:
            good.append(nearby_ticket)
            idx.append(i)

    print(good, 'LALLA')
    # good.remove(nearby_tickets[218])
    print(len(good))
    print(idx)
    # raise KeyError()

    possibles = [set(d.keys()) for _ in range(len(good[0]))]
    print(possibles)

    for j, good_ticket in enumerate(good):
        for i, item in enumerate(good_ticket):
            for key, (range1, range2) in d.items():
                if range1[0] <= item <= range1[1]:
                    continue
                if range2[0] <= item <= range2[1]:
                    continue
                if key in possibles[i]:
                    # if i == 1 and len(possibles[i]) == 1:
                    #     print(j, len(possibles[i]))

                    possibles[i].remove(key)

    # possibles2 = [set() for _ in range(len(good[0]))]
    #
    # for j, good_ticket in enumerate(good):
    #     for i, item in enumerate(good_ticket):
    #         for key, (range1, range2) in d.items():
    #             if key == 'class':
    #                 print('dd')
    #             if range1[0] <= item <= range1[1]:
    #                 possibles2[i].add(key)
    #             if range2[0] <= item <= range2[1]:
    #                 possibles2[i].add(key)
    #
    # if possibles2 != possibles:
    #     print('pop', possibles2, possibles)
    #     raise KeyError()
    #     pass

    # possibles = possibles2


    print(possibles)
    print('nina')

    old = [l.copy() for l in possibles]
    run = True
    while run:
        for i, st in enumerate(possibles):
            if len(st) == 1:
                itm = list(st)[0]
                for j, sety in enumerate(old):
                    if i==j:
                        continue
                    if itm in sety:
                        sety.remove(itm)
        if old == possibles:
            run = False
        possibles = [l.copy() for l in old]


    print(old, '\n',possibles)
    print('fuq')
    print(possibles)

    the_fields = [list(st)[0] for st in possibles]

    print('\n\n\n',the_fields)

    count = 1

    print('\n\n\n', the_fields, ticket)

    for field, num in zip(the_fields, ticket):
        print(field, num)
        if field.startswith('departure'):
            count*=num

    print('Count:', count)


# 1