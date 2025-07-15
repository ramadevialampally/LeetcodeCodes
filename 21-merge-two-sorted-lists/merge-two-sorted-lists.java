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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1==null && list2==null){
            return list1;
        }
        if(list1==null){
            return list2;
        }
        if(list2==null){
            return list1;
        }
        List<Integer> li=new ArrayList<>();
        while(list1!=null){
            li.add(list1.val);
            list1=list1.next;
        }
        while(list2!=null){
            li.add(list2.val);
            list2=list2.next;
        }
        Collections.sort(li);
        ListNode temp1=new ListNode(li.get(0),null);
        ListNode tem=temp1;
        for(int i=1;i<li.size();i++){
            tem.next=new ListNode(li.get(i),null);
            tem=tem.next;
        }
        return temp1;


        
    }
}