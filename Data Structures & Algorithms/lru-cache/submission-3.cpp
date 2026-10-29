class LRUCache {
public:
    class Node{
    public:
        int key = 0;
        int value = 0;
        Node *pre = NULL;
        Node *next = NULL;

    };
    Node *left = new Node; // least recenty used
    Node *right = new Node; // most recenty used
    
    unordered_map <int, Node*> cache;
    int max_capacity;
    
    LRUCache(int capacity) {
        cache.reserve(capacity);
        max_capacity = capacity;

        left -> next = right;
        right -> pre = left;
    }

    void remove(Node *node) { // remove at left
        Node *p = node -> pre;
        Node *n = node -> next;

        p -> next = n;
        n -> pre = p;
    }

    void insert(Node *node) { // inserta at right
       Node *p = right -> pre;
       p -> next = node;
       right -> pre = node;
       node -> next = right;
       node -> pre = p;
    }
    
    int get(int key) {
        auto it = cache.find(key);
        if (it != cache.end()) {
            remove(cache[key]);
            insert(cache[key]);
            return cache[key] -> value;
        }

        return -1;
    }
    
    void put(int key, int value) {
        auto it = cache.find(key);
        if (it != cache.end()) {
                remove(cache[key]);
        }
        cache[key] = new Node(key, value);
        insert(cache[key]);

        if (cache.size() > max_capacity) { // remove from the list and delete from HashMap then add new
                Node *del = left -> next;
                int del_key = del -> key;
                
                remove(del);
                delete del;
                cache.erase(del_key);
        }
    }
};
