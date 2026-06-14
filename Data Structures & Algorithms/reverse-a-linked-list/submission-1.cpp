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
    ListNode* reverseList(ListNode* head) {
        // get previous (new next)
        ListNode* prev = nullptr;
        // get curr
        ListNode* curr = head;

        while (curr){
            // save curr's next
            ListNode* temp = curr->next;
            // point curr at previous
            curr->next = prev;

            // update prev to be curr
            prev = curr;
            // update curr to be curr's next
            curr = temp;
        }

        return prev;
    }
};
