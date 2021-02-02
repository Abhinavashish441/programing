class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
def printlist(head):
    ptr = head
    while ptr:
        print(ptr.data,end='->')
        ptr = ptr.next
    print("none")
def pop(headref):
    
    result = headref.data
    headref = headref.next
    print('deleting....',result)
    return headref
if __name__=='__main__':
    head= None
    for i in reversed(range(1,5)):
        head = Node(i,head)
    
        head = pop(head)
    printlist(head)