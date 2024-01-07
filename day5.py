count = 0

with open('input.txt', 'r') as f:
    l = []
    lines = '''FBFBBFFRLR
FFFBBBFRRR
BBFFBBFRLL'''.split('\n')
    
    lines = f.readlines()
    mx = 0

    for line in lines:
        print('line', line[-1])
        line = line[:-1]
        curr = 0
        print(line[:-3])
        for i, letter in enumerate(line[:-3]):
            if letter == 'B':
                curr |= 1<<(6-i)

        curr2 = 0
        print(line[-3:])
        for i, letter in enumerate(line[-3:]):
            if letter == 'R':
                curr2 |= 1<<(2-i)

        print(curr, curr2)

        mx = max(mx, curr*8+curr2)
        l.append((curr*8+curr2))

    print('max:',mx)
    print(l)
    l.sort()

    print(l)
    idx = 0

    for num in l:
        if num+1 not in l and num + 2 in l:
            print('NUM', num+1)
    print('fak')

    for i in range(38,len(l)):
        if l[idx] != i:
            if l[idx] == i+1:
                print(i, l[idx], idx)
                break
            else:
                continue
        idx+=1
    # for i in range() 387


    # hi, low = 128, 0
    #
    # hi2, low2 = 7, 0
    #
    # mx = -1
    #
    # for line in lines:
    #     line = line[:-1]
    #     for letter in line[:-4]:
    #
    #         mid = (hi+low) // 2
    #         if letter == 'F':
    #             hi = mid
    #         else:
    #             low = mid
    #
    #         print(hi, low, mid)
    #
    #     if line[-4] == 'F':
    #         mid = low
    #     else:
    #         mid = hi
    #     print(mid)
    #     for letter in line[-3:-1]:
    #         mid2 = (hi2 + low2) // 2
    #         if letter == 'L':
    #             hi2 = mid2
    #         else:
    #             low2 = mid2
    #
    #     id = mid*mid2
    #     mx = max(mx, id)
    #     print(id, mx, mid, mid2)

    # print('Max', mx)


# 62




    print('Count:', count)

#7 - close
# 88= nope
#89
#243