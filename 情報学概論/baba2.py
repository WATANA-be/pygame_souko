MAX=5
stack = [None]*MAX
sp = 0

def push(d):
    global sp
    sp += 1
    stack[sp] = d
    print(stack)
    return stack[sp]

def pop():
    global sp
    d = stack[sp]
    del stack[sp]
    sp -= 1

    stack.append(None)
    print(stack)
    return(d)
    return stack[sp]

print(push(3))
print(push(8))
print(push(1))
print(pop())
print(pop())
print(push(5))