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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        int sum;
        int transfer = 0;
        ListNode *new_head = new ListNode;
        ListNode *help = new_head;
        while (l1 != NULL and l2 != NULL) {
            sum = l1 -> val + l2 -> val + transfer; /// if one ended add 0 do another 
            if (sum >= 10) {
                help -> val = sum % 10;
                transfer = 1;
            }
            else {
                help -> val = sum;
                transfer = 0;
            }
            if (l1 -> next != NULL and l2 -> next != NULL) {
                help -> next = new ListNode;            
                help = help -> next;
            }
            l1 = l1 -> next;
            l2 = l2 -> next;
        }

        while (l1 != NULL) {        
            help -> next = new ListNode;
            help = help -> next;
            sum = l1 -> val + transfer;
            if (sum >= 10) {
                help -> val = sum % 10;
                transfer = 1;
            }
            else {
                help -> val = sum;
                transfer = 0;
            }

            l1 = l1 -> next;
        }

        while (l2 != NULL) {
            help -> next = new ListNode;
            help = help -> next;
            sum = l2 -> val + transfer;
            if (sum >= 10) {
                help -> val = sum % 10;
                transfer = 1;
            }
            else {
                help -> val = sum;
                transfer = 0;
            }

            l2 = l2 -> next;
        }

        if (transfer == 1) {
            help -> next = new ListNode;
            help = help -> next;
            help -> val = 1;
        }

        return new_head;
    }
};
