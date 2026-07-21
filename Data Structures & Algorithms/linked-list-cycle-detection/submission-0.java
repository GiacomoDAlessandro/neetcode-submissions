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
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> set = new HashSet<>();

        ListNode slow = head;
        //fast = head.next;

        while (slow != null) {
            if (set.contains(slow)) {
                return true;
            }
            set.add(slow);
            slow = slow.next;
        }

        return false;
    }
}
