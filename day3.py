with open('input.txt', 'r') as f:
    lines = f.readlines()
    counts = []
    for delta_x, delta_y in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        count = 0
        curr_index = 0

        for i in range(0, len(lines), delta_y):
            line = lines[i]
            index = curr_index % 31
            print('line-1', line[-2])
            if line[index] == '#':
                print(curr_index)
                print(line, index, curr_index, len(line), line[index])
                count +=1
            curr_index += delta_x
        counts.append(count)



    print('Count:', counts)
    total_mul = 1
    for num in counts:
        total_mul *= num
    print(total_mul)

#7 - close
# 88= nope
#89
#243