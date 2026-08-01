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
    public void reorderList(ListNode head) {
        List<ListNode> list = new LinkedList<>();
        ListNode newNode = head;
        while (newNode != null) {
            list.add(newNode);
            newNode = newNode.next;
        }

        int i = 0;
        int j = list.size() - 1;
        List<ListNode> answer = new LinkedList<>();

        while (i < j) {
            list.get(i).next = list.get(j);

            i++;
            if (i == j) {
                break;
            }
            list.get(j).next = list.get(i);
            j--;
        }

        list.get(i).next = null;

        

    }
}
