/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head ==null){
            return head;
        }
        List<Integer>  li=new ArrayList<>();
        ListNode temp=head;
        while(temp!=null){
            li.add(temp.val);
            temp=temp.next;
        }
        ListNode ne=new ListNode(li.get(li.size()-1),null);
        temp=ne;
        for(int i=li.size()-2;i>=0;i--){
            temp.next=new ListNode(li.get(i),null);
            temp=temp.next;
            

        }
        return ne;
        
    }
}