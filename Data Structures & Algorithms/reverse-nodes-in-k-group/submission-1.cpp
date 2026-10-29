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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == NULL) return NULL;
        if (head->next == NULL) return head;    
        
        ListNode dummy(-1, head);
        ListNode *before = &dummy; // one node before group

        while (true) {
            ListNode *curr = before->next;
            ListNode *group[k];

            for (int i = 0; i < k; i++) {
                if (curr == NULL) return dummy.next;
                group[i] = curr;
                curr = curr->next;                
            }
            // remember what is after group
            ListNode *rem = curr;

            for (int i = k - 1; i > 0; i--) {
                group[i]->next = group[i-1];
            }

            before->next = group[k - 1];
            group[0]->next = rem;
            before = group[0];
        }
    }
};
