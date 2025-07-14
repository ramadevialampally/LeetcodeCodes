# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return head
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        b=a[:left-1]
        c=a[right:]
        k=a[left-1:right][::-1]
        print(b)
        print(k)
        print(c)
      
        res=[]
        for i in b:
            res.append(i)
        for i in k:
            res.append(i)
        for i in c:
            res.append(i)
        head=ListNode(res[0])
        temp=head
        for i in range(1,len(res)):
            temp.next=ListNode(res[i])
            temp=temp.next
        return head
                