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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        List<ListNode> list = new ArrayList<>();

        ListNode temp = head;

        while (temp != null) {
            list.add(temp);
            temp = temp.next;
        }

        int toRemove = list.size() - n;
        if (toRemove == 0) {
            return head.next;
        }

        ListNode newHead = head;

        for (int i = 0; i < list.size(); i++) {
            if (i == toRemove - 1) {
                head.next = head.next.next;
            } else {
                head = head.next;
            }
        }

        

        return newHead;
        
    }
}
