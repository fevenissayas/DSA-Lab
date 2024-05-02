class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    if head.next == None:
        return head
    iterator = head
    count = 1
    while head.next:
        head = head.next
        count += 1
    if count%2 == 0:
        count = count/2 + 1
    else:
        count = (count-1)/2+1

    temp = 1
    while temp<count:
        iterator = iterator.next
        temp += 1
        
    return iterator
        