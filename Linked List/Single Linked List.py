#Single Linked List

class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SList(object):
    def __init__(self):
        self.head = Node(None)
        self.size = 0
        
    def listSize(self):
        return self.size
    
    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True
        
    def selectNode(self, idx):
        if idx >= self.size:
            print("Index Error")
            return None
        if idx == 0:
            return self.head
        else:
            target = self.head
            for cnt in range(idx):
                target = target.next
            return target
        
    def appendleft(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.size += 1
    
    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        else:
            target = self.head
            while target.next != None:
                target = target.next
            newtail = Node(value)
            target.next = newtail
            self.size += 1
        
    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        elif idx == 0:
            self.head = Node(value, self.head)
            self.size += 1
        else:
            target = self.selectNode(idx-1)
            if target == None:
                return
            newNode = Node(value)
            tmp = target.next
            target.next = newNode
            newNode.next = tmp
            self.size += 1
        
    def delete(self, idx):
        if self.is_empty():
            print('Underflow: Empty Linked List Error')
            return
        elif idx > self.size:
            print('Overflow: Index Error')
            return
        elif idx == 0:
            target = self.head
            self.head = target.next
            del(target)
        else:
            target = self.selectNode(idx-1)
            target.next = target.next.next
            deltarget = target.next
            del(deltarget)
            
    def printlist(self):
        target = self.head
        while target:
            if target.next != None:
                print(target.data, '-> ', end='')
                target = target.next
            else:
                print(target.data)
                target = target.next
                
mylist = SList()
mylist.append('A')
mylist.printlist()
mylist.append('B')
mylist.printlist()
mylist.append('C')
mylist.printlist()
mylist.insert('D', 1)
mylist.printlist()
mylist.appendleft('E')
mylist.printlist()
print(mylist.listSize())
mylist.delete(0)
mylist.printlist()
mylist.delete(3)
mylist.printlist()
mylist.delete(0)
mylist.printlist()
mylist.appendleft('A')
mylist.printlist()
