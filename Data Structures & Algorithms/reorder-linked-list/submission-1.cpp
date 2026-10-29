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
        ListNode *help = head;
        int n = 0;
        while (help != NULL) {
            n++;
            help = help->next;
        }

        ListNode *tab[n] = {};
        help = head;
        for (int i=0; i<n; i++) {
            tab[i] = help;
            help = help->next;
        }

        int s = 0;
        int e = n - 1;
        while (s < e) {
            tab[s]->next = tab[e];
            s++;
            tab[e]->next = tab[s];
            e--;
        }
        tab[s]->next = NULL;        
    }
};
