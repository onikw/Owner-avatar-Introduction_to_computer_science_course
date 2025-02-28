class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def member(zb, el):
    x = zb
    while x != None and x.val < el:
        x = x.next
    return x != None and x.val == el


x = Node(23)


def insert(a, el):
    zb = a
    t = None
    while zb != None and zb.val < el:
        t = zb
        zb = zb.next
    if t != None and t.val == el:
        return

    x = Node(el)
    x.next = zb
    if t != None:
        t.next = x
        return a
    else:
        return x
