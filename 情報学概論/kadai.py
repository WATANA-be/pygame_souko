sp = 0
MAX = 6
stack = [0]*MAX

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp += 1
        print(stack)
def pop():
    global sp 
    if sp > 0:
        sp -= 1
        return stack[sp]
        print(stack)
    else:
        return None

push(3)
push(8)
push(1)
pop()
pop()
push(5)