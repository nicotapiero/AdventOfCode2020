count = 0

def get_clockwise_after_one(l):
    index_of_one = l.index(1)


    curr = (index_of_one+1) % len(l)
    s = []
    while curr != index_of_one:
        # print(l, s, curr)
        s.append(l[curr])
        curr +=1
        curr = curr % len(l)
    return ''.join([str(let) for let in s])

# print('nig',get_clockwise_after_one([5,8, 3,  7,  4,  1,  9,  2,  6 ]))


with open('input.txt', 'r') as f:
    l = []

    lines = '''963275481'''

    # lines = f.readlines() # comment out this line to run above test case
    #
    # lines = [line[:-1] if line[-1] == '\n' else line for line in lines]

    cups = [int (i) for i in lines]

    for i in range(10, 100):
        cups.append(i)

    print(cups)
    turn = 0

    for _ in range(10):
        turn_value = cups[turn]
        print('\n', count+1, 'FUCK', cups)
        print('Turn for cup %d, which is %d' % (cups[turn], turn), cups)
        pickup = []
        popper = (turn + 1) % len(cups)
        for i in range(1,4):
            print(popper, cups, len(cups))

            pickup.append(cups.pop(popper))
            popper = (popper) % len(cups)
        print(pickup)

        # print('old cups', cups, destination)
        destination = -1
        sub= turn_value - 1
        min_label = min(cups)
        max_label = max(cups)
        while destination == -1:
            try:
                destination = cups.index(sub)

            except:
                pass
            sub -= 1

            if sub < min_label:
                sub = max_label
        destination = (destination + 1)
        print('old cups', cups, destination)
        print(destination)
        cups = cups[:destination] + pickup + cups[destination:]
        print('new cups', cups)

        # turn += 1
        # if destination < turn -1:
        #     turn +=3
        # turn = turn % len(cups)
        print(cups.index(turn_value)+ 1 % len(cups))
        turn = (cups.index(turn_value) + 1) % len(cups)
        count+=1

    print('ANSWER', get_clockwise_after_one(cups))

    print('Count:', count)

# List of Wrong Answers:
#