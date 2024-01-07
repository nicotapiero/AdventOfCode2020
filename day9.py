count = 0

def two_sum(l, target):
    s = set()

    for num in l:
        if target-num in s:
            return True
        s.add(num)
    return False

with open('input.txt', 'r') as f:
    l = []
    lines = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''.split('\n')
    
    lines = f.readlines()

    l = [int(i) for i in lines[:25]]

    for i in range(len(lines)):
        l = [int(lines[i])]
        j = i + 1
        while sum(l) < 104054607:
            print(l)
        # while sum(l) <= 104054607:
            l.append(int(lines[j]))
            j += 1
        print(sum(l))
        if sum(l) == 104054607:
            print(l)
            print('ans', min(l) , max(l))
            break

    # for line in lines[25:]:
    #     num = int(line)
        # if two_sum(l, num):
        #     l.pop(0)
        #     l.append(num)
        # else:
        #     print(num)
        #     break

    print('Count:', count)
