sp = 0
MAX = 5
stack = [None]*MAX


def pop():
    global sp 
    #print("a")
        sp = sp- 1
        return stack[sp]
        del stack[None]
        print(stack)
        #print(d)
        #print("a")
    else:
        return None
        #print("あ")
    print(stack)
    print(stack[sp])

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp =sp+ 1
        #del stack[None]
        print(stack)
        print(stack[sp])
        #print(d)

push(3)
push(8)
push(1)
pop()
pop()
push(5)