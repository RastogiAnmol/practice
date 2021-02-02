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


lst = [None] * 10

push(lst, 1)
push(lst, 2)
push(lst, 3)
push(lst, 4)
push(lst, 5)
push(lst, 6)
push(lst, 7)
push(lst, 8)
push(lst, 9)
push(lst, 10)
print("Before pop")
display(lst)
print("after popping element", pop(lst))
display(lst)
print("after popping another element", pop(lst))
display(lst)
