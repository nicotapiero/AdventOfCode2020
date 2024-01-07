count = 0

def parser(s):
    pass

subject_number = 7

def perform_steps(value):
    value = value * subject_number
    value = value % 20201227
    return value



with open('input.txt', 'r') as f:
    l = []

    lines = '''17607508
15065270'''.split('\n')

    # lines = f.readlines() # comment out this line to run above test case
    #
    # lines = [line[:-1] if line[-1] == '\n' else line for line in lines]

    lines = [int(i) for i in lines]

    # lines = [5764801, 17807724]

    [card_key, door_key] = lines

    curr = 1
    card_loop_size = 0
    while curr != card_key:
        curr = perform_steps(curr)
        card_loop_size +=1
    print(curr,card_loop_size,'\n')

    curr = 1
    door_loop_size = 0
    while curr != door_key:
        curr = perform_steps(curr)
        door_loop_size += 1

    print(curr, door_loop_size, '\n')

    # curr = 17807724
    subject_number = door_key
    curr = 1
    for _ in range(card_loop_size):
        curr = perform_steps(curr)

    print(curr)

    print('Count:', count)

# List of Wrong Answers:
#