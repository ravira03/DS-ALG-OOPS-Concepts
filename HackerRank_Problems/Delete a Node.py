def deleteNode(llist, position):
    if position == 0:
        llist = llist.next
    else:
        node = llist
        for _ in range(position-1):
            node = node.next
        
        node.next = node.next.next
        
    return llist
