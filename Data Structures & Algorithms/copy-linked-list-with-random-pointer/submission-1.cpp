/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL) return NULL;
        Node *old = head;
        Node *new_head = new Node(-1);
        Node *nev = new_head;

        while (old != NULL) {
            nev->val = old->val;
            if (old->next != NULL) {
                nev->next = new Node(-1);
            }            
            old = old->next;
            nev = nev->next;
        }

        unordered_map <Node*, int> random1;
        unordered_map <int, Node*> random2;
        int i = 0;

        old = head;
        while (old != NULL) {
            random1[old] = i;
            i++;
            old = old->next;
        }

        nev = new_head;
        i = 0;
        while (nev != NULL) {
            random2[i] = nev;
            i++;
            nev = nev->next;
        }

        nev = new_head;
        old = head;
        i = 0;
        while (nev != NULL) {
            if (old->random != NULL)
                nev->random = random2[random1[old->random]];
            nev = nev->next;
            old = old->next;
        }

        return new_head;
    }
};
