count = 1

from collections import defaultdict, deque

cups = '''963275481'''
cups = deque([int (i) for i in cups])

# 10,000,000 cups, but it's one indexed so it'll include the 10,000,000
for i in range(10, 1000000+1):
    cups.append(i)

personal_next_cache = defaultdict(list)

def get_next_cup():
    num = cups.popleft()

    # dump the cache if theres stuff that comes after it
    if num in personal_next_cache:
        # extendleft adds the list in reversed order, so we want to push them
        # on in their original order. So we should add them reversed
        # alternatively could do like:
        #   while personal_next_cache[num]: cups.appendleft(personal_next_cache[num].pop())
        # if that makes more sense to you
        cups.extendleft(list(reversed(personal_next_cache[num])))
        del personal_next_cache[num]
    return num

for _ in range(10000000):
    print('Current Turn:', count)

    current_cup = get_next_cup()
    pickup = [get_next_cup(), get_next_cup(), get_next_cup()]

    cant_use = {current_cup, pickup[0], pickup[1], pickup[2]}

    destination = current_cup-1 if current_cup > 1 else 1000000
    while destination in cant_use:
        destination -=1
        if destination < 1:
            destination = 1000000

    # add the cups to the end of the one they follow
    personal_next_cache[destination].extend(pickup)

    # add the current cup to the back of the queue
    cups.append(current_cup)

    count+=1

# Find the 1. It might be in someone's personal_next_queue, so we need to make
# sure to take things off the queue in order
search = get_next_cup()
while search != 1:
    cups.append(search)
    search = get_next_cup()

following_1, following_2 = get_next_cup(), get_next_cup()

print(following_1, following_2)