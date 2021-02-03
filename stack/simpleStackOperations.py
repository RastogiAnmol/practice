top: int = -1


def stack_empty():
    return -1 == top


def push(s, x):
    # use global keyword to access global variables
    global top
    if top == len(s) - 1:
        print("overflow")
        return
    top = top + 1
    s[top] = x


def pop(s):
    if stack_empty():
        print("underflow")
        return
    else:
        global top
        top = top - 1
        popped_element = s[top + 1]
        s[top + 1] = None
        return popped_element


def display(s):
    count = top
    while count != -1:
        element = s[count]
        print(element)
        count -= 1


stack = [None] * 10

push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)
push(stack, 5)
push(stack, 6)
push(stack, 7)
push(stack, 8)
push(stack, 9)
push(stack, 10)

print("Before pop")
display(stack)
print("after popping element", pop(stack))
display(stack)
print("after popping another element", pop(stack))
display(stack)
