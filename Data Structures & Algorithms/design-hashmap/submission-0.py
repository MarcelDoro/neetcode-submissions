class Node:
    def __init__(self, key: int, value: int = 0):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.hash_map = [Node(i) for i in range(10_000)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % len(self.hash_map)
        node = self.hash_map[hash_key]
        while node.next:
            if node.next.key == key:
                node.next.value = value
                return

            node = node.next
        node.next = Node(key, value)

    def get(self, key: int) -> int:
        hash_key = key % len(self.hash_map)
        node = self.hash_map[hash_key].next
        while node:
            if node.key == key:
                return node.value

            node = node.next

        return -1

    def remove(self, key: int) -> None:
        hash_key = key % len(self.hash_map)
        node = self.hash_map[hash_key]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return

            node = node.next                

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)