def insertNodeAtHead(llist, data):
    
    x = SinglyLinkedListNode(data)
    if(llist == None):
        llist = x
    else:
        new_node = x
        new_node.next = llist
        llist = new_node
    return llist

