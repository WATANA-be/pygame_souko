MAX=5
stack = [None]*MAX
sp = 0

def push(d):
    global sp
    sp += 1
    stack[sp] = d
    print(stack)

def pop():
    global sp
    d = stack[sp]
    del stack[sp]
    sp -= 1

    stack.append(None)
    print(stack)
    return(d)
print(push(3))
push(8)
push(1)
pop()
pop()
push(5)