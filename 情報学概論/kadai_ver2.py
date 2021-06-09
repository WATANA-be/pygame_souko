sp = 0
MAX = 6
stack = [None]*MAX


def pop():
    global sp 
    #print("a")
    if sp > 0:
        sp = sp- 1
        
        #del stack[None]
        print(stack)
        return stack[sp]
        #print(d)
        #print("a")
    else:
        print(stack)
        print(stack[sp])
        return None
        #print("あ")
    #print(stack)
    #print(stack[sp])

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