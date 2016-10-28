from vaje3 import Queue

def queueMerge(l):
    if len(l) == 0:
        return l
    q = Queue()
    for x in l:
        q.enqueue([x])
    while len(q) > 1:
        a = q.dequeue()
        b = q.dequeue()
        i, j = 0, 0
        c = []
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        c += a[i:] + b[j:]
        q.enqueue(c)
    return q.dequeue()
