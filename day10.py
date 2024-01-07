count = 0

def count_paths(l, curr):
    if not l or (curr+1 not in l and curr+2 not in l and curr+3 not in l):
        return 1

    ways = 0

    # print(curr, sorted(l), len(l))

    if curr + 1 in l:
        copy = l.copy()
        copy.remove(curr + 1)
        ways += count_paths(copy, curr+1)

    # print(curr, ways)
    if curr + 2 in l:
        copy = l.copy()
        copy.remove(curr + 2)
        ways += count_paths(copy, curr + 2)

    # print(curr, ways)
    if curr + 3 in l:
        copy = l.copy()
        copy.remove(curr + 3)
        ways += count_paths(copy, curr + 3)

    # print(curr, ways)

    return ways

with open('input.txt', 'r') as f:
    l = []
    lines = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.split('\n')

#     lines = '''16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4'''.split('\n')
    
    lines = f.readlines()

    lines = [int(line) for line in lines]

    lines.append(0)
    lines.append(max(lines)+3)

    # ways = count_paths(lines, 0)
    # print(len(lines))

    longest_path = sorted(lines)

    dp = [0] * len(longest_path)
    dp[0] = 1

    for i in range(1, len(longest_path)):
        # dp[i] = dp[i-1]
        num = longest_path[i]
        if num-1 in longest_path:
            dp[i] += dp[longest_path.index(num-1)]
        if num-2 in longest_path:
            dp[i] += dp[longest_path.index(num-2)]
        if num-3 in longest_path:
            dp[i] += dp[longest_path.index(num-3)]
        # if i > 0:
        #     if longest_path[i]-1 == longest_path[i-1]:
        #         dp[i] += dp[i-1]
        # if i > 1:
        #     if longest_path[i]-2 == longest_path[i-2]:
        #         dp[i] += dp[i-2]
        # if i > 2:
        #     if longest_path[i]-3 == longest_path[i-3]:
        #         dp[i] += dp[i-3]
        # dp[i] = max(dp[i-1], dp[i])


    # for i, num in enumerate(longest_path):
    #
    #     if i < len(longest_path)-1:
    #         if longest_path[i+1] == num +1:
    #             ways += 2
    #     if i < len(longest_path)-2:
    #         if longest_path[i+2] == num +2:
    #             ways += 2
    #     if i < len(longest_path)-3:
    #         if longest_path[i+3] == num +3:
    #             ways += 2

    print(dp)
    print(longest_path)
    print('ans', dp[-1])
    # print(count_1, count_3)




    print('Count:', count)

#174