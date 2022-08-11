def insertNodeAtTail(head, data):
    n = SinglyLinkedListNode(data)
    if head == None:
        head = n
    else:
        t = head
        while t.next != None:
            t = t.next
        t.next = n
    return head


def insertNodeAtHead(llist, data):
    n = SinglyLinkedListNode(data)
    if llist:
        n.next = llist
    return n


def deleteNode(llist, position):
    if position == 0:
        llist = llist.next
    else:
        t = llist
        count = 1
        while t != None and count < position:
            t = t.next
            count += 1
        t.next = t.next.next

    return llist
