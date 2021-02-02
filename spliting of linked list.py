#Spliting of linked list
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
def printlist(msg,head):
    ptr=head
    while ptr:
        print(ptr.data, end="->")
        ptr = ptr.next
    print('Null')
def length(head):
    count=0
    ptr = head
    while ptr:
        count += 1
        ptr=ptr.next
    return count
def spilt(source):
    lent = length(source)
    if lent<2:
        front=source
        back=None
        return front,back
    current = source
    hopcount=(lent-1)//2
    for i in range(hopcount):
        current = current.next
    back = current.next
    current.next=None
    front = source
    return front,back
if __name__=='__main__':
    keys = [6,7,8,9,5,4,5,6]
    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i],head)
    first, second = spilt(head)
    printlist("Front list=: ", first)
    printlist("Backlist=: ",second)
        
    