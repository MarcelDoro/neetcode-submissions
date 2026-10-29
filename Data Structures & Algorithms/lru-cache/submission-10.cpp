class LRUCache {
public:
    class Node {
    public:
        int key = -1;
        int value = -1;
        Node *pre = NULL;
        Node *next = NULL;
    };

    int max_capacity = 0;
    unordered_map <int, Node*> cache;
    Node *left, *right;
    
    LRUCache(int capacity) {        
        max_capacity = capacity;
        cache.reserve(capacity);       
        left = new Node;
        right = new Node; 
        left -> next = right;
        right -> pre = left;        
    }

    void remove(Node *node) {
        Node *p = node -> pre;
        Node *n = node -> next;
        
        p -> next = n;
        n -> pre = p;
    }
    
    void insert(Node *node) {
        Node *p = right -> pre;
        p -> next = node;
        node -> next = right;
        node -> pre = p;
        right -> pre = node;
        
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
        if (it != cache.end()) { // if key is already in cache
            cerr << it -> first << " " << it -> second << endl;
            remove(cache[key]);
            delete cache[key];
            cache[key] = new Node;
            cache[key] -> key = key;
            cache[key] -> value = value;
            insert(cache[key]);
        }
        else if (cache.size() >= max_capacity) { // if we exceed maximal capacity
            Node *del = left -> next;
            cache.erase(del->key);
            remove(del);
            delete del;
            
            cache[key] = new Node;
            cache[key] -> key = key;
            cache[key] -> value = value;
            insert(cache[key]);
        }
        else {
            cache[key] = new Node;
            cache[key] -> key = key;
            cache[key] -> value = value;
            insert(cache[key]);
        }
    }
};
