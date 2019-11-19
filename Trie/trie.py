#Trie Data Structure
from collections import deque

class Node(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.child = {}

class Trie(object):
    def __init__(self, string):
        self.head = Node(None)
        
    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.child:
                curr_node.child[char] = Node(char)
            curr_node = curr_node.child[char]
        curr_node.data = string
    
    def search(self, string):
        curr_node = self.head
        for char in string:
            if char in curr_node.child:
                curr_node = curr_node.child[char]
            else:
                return False
        if curr_node.data != None:
            return True
    
    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None
        
        for char in prefix:
            if char in curr_node.child:
                curr_node = curr_node.child[char]
                subtrie = curr_node
            else:
                return None
        
        q = deque(subtrie.child.values())
        while q:
            curr = q.popleft()
            if curr.data != None:
                result.append(curr.data)
            q += list(curr.child.values())
            
        return result
