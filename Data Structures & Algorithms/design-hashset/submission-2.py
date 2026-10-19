class ListNode:
    def __init__(self, value: int = -1):
        self.value = value
        self.next = None


class MyHashSet:

    def __init__(self):
        self.set = [ListNode(-1) for _ in range(10**4)]

    def add(self, key: int) -> None:        
        node = self.set[key % len(self.set)]
        while node.next:
            if node.next.value == key:
                return

            node = node.next
        
        node.next = ListNode(key)  
        print("add.end")          

    def remove(self, key: int) -> None:
        node = self.set[key % len(self.set)]
        while node.next:
            if node.next.value == key:
                node.next = node.next.next
                return

            node = node.next    

        print("remove.end")                         
        
    def contains(self, key: int) -> bool:
        node = self.set[key % len(self.set)]
        while node.next:
            if node.next.value == key:
                return True

            node = node.next

        return False
        print("contains.end")          


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)