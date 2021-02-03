"""check figure of clrs page 202
    This program assumes tail to be the last element rather than first element where we can insert value
"""
head = tail = -1


def enqueue(q, x):
    global head, tail
    if check_overflow(q):
        print("overflow")
        return
    elif tail == len(q) - 1:
        tail = 0
    else:
        if head == tail == -1:
            head = head + 1
        tail = tail + 1
    q[tail] = x


def dequeue(q):
    global head, tail
    if check_underflow():
        print("underflow")
        return
    x = q[head]
    q[head] = None
    if head == tail:
        head = tail = -1
    elif head == len(q) - 1:
        head = 0
    else:
        head = head + 1
    return x


def check_overflow(q):
    if head < tail:
        count = tail - head + 1
    else:
        count = (len(q) - head) + (tail + 1)

    return count == len(q)


def check_underflow():
    return head == tail == -1


def display(q):
    if head <= tail:
        for i in range(head, tail + 1):
            print(q[i])
    else:
        for i in range(head, len(q)):
            print(q[i])
        for i in range(tail + 1):
            print(q[i])


queue = [None] * 10

enqueue(queue, 1)
enqueue(queue, 2)
enqueue(queue, 3)
enqueue(queue, 4)
enqueue(queue, 5)
enqueue(queue, 6)
enqueue(queue, 7)
enqueue(queue, 8)
enqueue(queue, 9)
enqueue(queue, 10)

# the below line will overflow
enqueue(queue, 11)

print("===============before dequeue===============")
display(queue)
print("===============after dequeue================")

dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)

display(queue)

print("===============enqueue again================")
enqueue(queue, 1)
enqueue(queue, 2)
display(queue)

print("===============dequeue again================")
enqueue(queue, 3)
enqueue(queue, 4)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)

display(queue)
