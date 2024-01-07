def two_sum(target, list):
    s = set()
    for line in list:
        i = int(line)

        if target - i in s:
            return (i * (target - i))

        s.add(i)

    return float('inf')

with open('input.txt', 'r') as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        i = int(line)
        ret = two_sum(2020-i, lines[:i])
        if ret != float('inf'):
            print(i)
            print(i*ret)



