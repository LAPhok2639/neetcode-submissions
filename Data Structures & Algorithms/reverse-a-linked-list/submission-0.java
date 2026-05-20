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
        ListNode prev = null;
        ListNode current = head;

        
        while (current != null) { // null (prev) // 10 (current) → 20 → 30 → null
            ListNode temp = current.next; // null (prev) // 10 (current) → 20 (temp) → 30 → null
            current.next = prev; // 10 (current) → null (prev) // 20 (temp) → 30 → null
            prev = current; // 10 (current, prev) → null // 20 (temp) → 30 → null
            current = temp; // 10 (prev) → null // 20 (temp, current) → 30 → null
        }
        return prev;  
    }
}
