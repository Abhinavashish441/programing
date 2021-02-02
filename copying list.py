class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
def printlist(head):
    ptr= head
    while ptr:
        print(ptr.data,end="->")
        ptr=ptr.next
    print("None")
def copylist(head):
    current = head
    newlist = None
    tail = None
    while current:
        if newlist is None:
            newlist=Node(current.data, None)
            tail=newlist
        else:
            tail.next = Node()
            tail = tail.next
            tail.data=current.data
            tail.next = None
        current = current.next
    return newlist
if __name__ =='__main__':
    head = None
    for i in reversed(range(4)):
        head = Node(i+1,head)
    copy = copylist(head)
    printlist(copy)
    