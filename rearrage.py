#rearrage the given linked list 
class Node:
    def __init__(self,data=None,next = None):
        self.data= data
        self.next = next
def printlist(msg, head):
    
    print(msg, end="")
    ptr=head
    while ptr:
        print(ptr.data, end="->")
        ptr=ptr.next
    print('null')
def rearrage(head):
    if head is None:
        return head
    odd = head
    even = None
    prev = None
    while odd and odd.next:
        if odd.next:
            newnode = odd.next
            odd.next = odd.next.next
            newnode.next= even
            even=newnode
        prev = odd
        odd= odd.next
    if odd:
        odd.next=even
    else:
        prev.next = even
    return head
if __name__ == '__main__':
    head = None
    for i in reversed(range(8)):
        head=Node(i+1,head)
    printlist("before: ", head)
    head = rearrage(head)
    printlist("After: ",head)
    

        