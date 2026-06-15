/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next || !head->next->next) return;
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next){
            slow = slow->next;
            fast = (fast->next)->next;
        }

        ListNode* second = slow->next;
        slow->next = nullptr; // Sever the connection completely

        ListNode* prev = nullptr;
        while (second) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }
        
        ListNode* l1 = head;
        ListNode* l2 = prev;
        
        while (l1 && l2) {
            ListNode* t1 = l1->next;
            ListNode* t2 = l2->next;

            l1->next = l2;       // Connect current L1 node to L2 node
            if (!t1) break;      // If L1 is exhausted, we are done
            l2->next = t1;       // Connect L2 node back to the next L1 node

            l1 = t1;
            l2 = t2;
        }
    }
};
