count = 0

def solve(s):
    stack = []
    splits = s.split(' ')
    i=0
    while i < len(splits):
        split = splits[i]
        if split.startswith('('):
            j = i

            # Balanced parentheses
            num_open = 0
            for char in split:
                if char == '(':
                    num_open += 1
            j+=1
            while num_open > 0:
                for char in splits[j]:
                    if char == ')':
                        num_open -= 1
                    if char == '(':
                        num_open += 1
                j += 1

            # Recursively call on smaller string
            ans = solve(' '.join(splits[i:j])[1:-1])

            # If when you append, there's a + on the top of the stack, greedily resolve it
            stack.append(ans)
            if len(stack) > 2 and stack[-2] == '+':
                ans = stack[-1] + stack[-3]
                stack.pop(); stack.pop(); stack.pop()
                stack.append(ans)
            i = j

        #if it's a number, greedily resolve +'s otherwise add to stack
        elif split.isdigit():
            num = int(split)
            if not stack:
                stack.append(num)
                i += 1
                continue
            if stack[-1] == '+':
                ans = num + stack[-2]
                stack.pop(); stack.pop()
                stack.append(ans)
            else:
                stack.append(num)
            i+=1

        # always add operations to the stack
        else:
            stack.append(split)
            i+=1

    return solve_stack(stack)

def solve_stack(stack):
    # Invariant: stack should never have a + when it is evaluated, those should have been greedily resolved prior
    if '+' in stack:
        raise KeyError

    while len(stack) > 1:
        num = stack.pop()
        if stack[-1] == '+':
            ans = num + stack[-2]
        else:
            ans = num * stack[-2]
        stack.pop();
        stack.pop()
        stack.append(ans)
    return stack[0]

with open('input.txt', 'r') as f:
    l = []

    lines = '''7 * 6 + ((8 + 6 * 6 + 2 + 3) + 9 * (2 * 4 * 8 * 4)) + 8 * 6 + 9'''.split('\n')

    lines = f.readlines() # comment out this line to run above test case

    lines = [line[:-1] if line[-1] == '\n' else line for line in lines]

    for line in lines:
        count += solve(line)

    print('Count:', count)

# List of Wrong Answers:
# 45587434237590
# 45840329911668
# 45840336521334

# 321712389977803
# 328918568107734