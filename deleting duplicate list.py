#Delete duplicate Node of linked list
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
def printlist(head):
    ptr= head
    while ptr:
        print(ptr.data, end = '->')
        ptr = ptr.next
    print('Null')
def deleting(head):
    current =head
    if head is None:
        return head
    
    while current.next:
        if current.data==current.next.data:
            x = current.next.next
            current.next = x
        else:
            current = current.next
    return head
if __name__=='__main__':
    head = None
    keys = [1,2,2,3,3,4,5]
    for i in reversed(range(len(keys))):
        head= Node(keys[i],head)
    y= deleting(head)
    printlist(y)
    
    