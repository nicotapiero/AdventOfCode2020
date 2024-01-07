count = 0

from collections import defaultdict

with open('input.txt', 'r') as f:
    l = []
    lines = '''10,16,6,0,1,17'''.split(',')

    
    # lines = f.readlines()

    ages = {}

    for i, num in enumerate(lines):
        ages[int(num)] = (i+1, i+1)

    # print(ages)

    last = int(lines[-1])

    for i in range(7, 30000000+1):
        # if last not in ages:
        #     nxt = 0
        age_of_last = ages[last][0] - ages[last][1]
        # print(age_of_last, last, ages)

        if age_of_last == 0:
            nxt = 0
        else:
            nxt = age_of_last

        if nxt not in ages:
            ages[nxt] = (i,i)
        else:
            ages[nxt] = (i, ages[nxt][0])
        # print(last, nxt, ages)
            # ages[nxt] = (i, ages[nxt][0])

        last = nxt
        # print('turn' , i, last, age_of_last, ages[last], last)
    print(last)



    print('Count:', count)


# 1