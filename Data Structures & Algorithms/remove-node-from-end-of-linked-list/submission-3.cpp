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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // track dummy
        ListNode* dummy = new ListNode(0, head);

        // track prev
        ListNode* prev = dummy;
        ListNode* curr = head;
        ListNode* fast = head;

        // n gap between curr & fast
        for (int i = 0; i < n; i++){
            fast = fast->next;
            if ((i+1) < n && !fast){
                return head;
            }
        }

        // iterate all ptrs forward
        while (fast){
            prev = curr;
            curr = curr->next;
            fast = fast->next;
        }
        
        // remove nth from end (curr)
        prev->next = curr->next;
        delete curr;
        curr = nullptr;

    
        return dummy->next;
    }   
};
