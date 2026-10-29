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
    bool listsEnd(vector<ListNode*>& lists) {
        int n = lists.size();

        for (int i=0; i<n; i++) {
            if (lists[i] != NULL) return false;
        }

        return true;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        for (int i=0; i<lists.size(); i++)
                if (lists[i] != NULL)
                    cerr << "list " << i << " value " << lists[i] -> val << endl;

        int n = lists.size();        
        ListNode *head = NULL;
        ListNode *help = head;

        for (int i=0; i<n; i++)
                if (lists[i] != NULL)
                    cerr << "list " << i << " value " << lists[i] -> val << endl;

        while (listsEnd(lists) == false) { // while there are nodes in lists    
            for (int i=0; i<n; i++)
                if (lists[i] != NULL)
                    cerr << "list " << i << " value " << lists[i] -> val << endl;

            int starting = 0;
            while (lists[starting] == NULL) starting++;

            int listNumber = starting;            
            int mini = lists[starting] -> val;

            for (int i=starting; i<n; i++) {                              
                if (lists[i] != NULL && lists[i] -> val < mini) {
                    mini = lists[i] -> val;
                    listNumber = i;
                }
            }

            cerr << listNumber << endl;

            if (head == NULL) {
                head = lists[listNumber];
                help = head;   
            } else {                  
                help -> next = lists[listNumber];
                help = help -> next;                
            }
            lists[listNumber] = lists[listNumber] -> next;             
        }        

        return head;
    }
};
