#Trie 2

from collections import defaultdict


class Node:
    def __init__(self, label=None, data=None):
        self.label = label
        self.data = data
        self.children = defaultdict(Trie)
        self.NodeCount = 0

    def add_child(self, key, data=None):
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key

    def __getitem__(self, key):
        return self.children[key]

    def __str__(self, depth=0):
        s = []
        for key in self.children:
            s.append('{}{} {}'.format(' ' * depth, key or '#', '\n' + self.children[key].__str__(depth + 1)))
        return ''.join(s)
    
class Trie:
    def __init__(self):
        self.head = Node()

    def __getitem__(self, key):
        return self.head.children[key]

    def __str__(self, depth=0):
        return self.head.__str__()

    def add(self, word):
        current_node = self.head
        word_finished = True

        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break

        if not word_finished:
            while i < len(word):
                current_node.add_child(word[i])
                current_node.NodeCount += 1
                current_node = current_node.children[word[i]]
                i += 1

        current_node.add_child(None)
        current_node.NodeCount += 1
        current_node = current_node.children[None]
        current_node.data = word

    def insert_word(self, word):
        for word in word.split():
            self.add(word)
            
if __name__ == '__main__':
    trie = Trie()
    trie.insert_word('stan stem standard money')

    print(trie)
