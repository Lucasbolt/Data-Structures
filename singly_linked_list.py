#demonstrating singly-linked list.

class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.head = None

    #method for setting data field for node
    def setData(self, data):
        self.data = data

    #method for getting data field of the node
    def getData(self):
        return self.data

    #method for setting the next field of the node
    def setNext(self, node):
        self.next = node

    #method for getting the next field of the node
    def getNext(self):
        return self.next
    
    #returns True if the node points to another node
    def hasNext(self):
        return self.next != None

    #method for counting the number of nodes in a linked-list
    def listLength(self, node):
        current = node
        count = 0
        while current != None:
            count+=1
            current = current.getNext()
        return count

    #method for inserting a new node at the beginning of linked list
    def insertAtBeginning(self, data):
        newnode = Node()
        newnode.setData(data)
        
        if self.length == 0:
            self.head = newnode
        else:
            newnode.setNext(self.head)
            self.head = newnode
        self.length+=1

    #method for inserting a new node at the end of linked list
    def insertAtEnd(self, data):
        newnode = Node()
        newnode.setData(data)
        current = self.head
        while current.getNext()!= None:
            current = current.getNext()
        current.setNext(newnode)
        self.length+=1
    
    #method for inserting a new node at a given position(pos)
    def insertAtPos(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newnode = Node()
                    newnode.setData(data)
                    count = 0
                    current = self.head
                    while count < pos-1:
                        current.getNext()
                    newnode.setNext(current.getNext())
                    current.setNext(newnode)
                    self.length+=1
    
    #method to delete first node in a linked list
    def deleteFirstNode(self):
        if self.length == 0:
            raise ValueError('the list is empty...')
        else:
            self.head = self.head.getNext()
            self.length-=1
    
    #method to delete the last node of the linked list
    def deleteLastNode(self):
        if self.length == 0:
            raise ValueError('the list is empty...')
        else:
            currentnode = previous = self.head
            while currentnode.getNext() != None:
                previous = currentnode
                currentnode = currentnode.getNext()
            previous.setNext(currentnode.getNext())
            self.length-=1

    #delete with node from linked list
    def deleteFromLinkedListWithNode(self, node):
        if self.length == 0:
            raise ValueError('the list is empty...')
        else:
            currentnode = self.head
            previous = None
            found = False

            while not found:
                if currentnode == node:
                    found = True
                elif currentnode is None:
                    print('the node does not exist in the list...')
                else:
                    previous = currentnode
                    currentnode = currentnode.getNext()
            
            if previous is None:
                self.head = currentnode.getNext()
            else:
                previous.setNext(currentnode.getNext())
            self.length-=1
    
    #delete with data from linked list
    def deleteValue(self, value):
        currentnode = previous = self.head

        while currentnode.getNext() != None or currentnode.getData() != value:
            if currentnode.getData() == value:
                previous.getNext() == currentnode.getNext()
                self.length -= 1
                return
            else:
                previous = currentnode
                currentnode = currentnode.getNext()
        print('the value is not present...')
    
    #method to delete a node at a particular position
    def deleteNodeAtPos(self, pos):
        count = 0
        currentnode = previous = self.head
        if pos > self.length or pos < 0:
            print('The position does not exist. Enter a valid position...')
        else:
            while currentnode.getNext()!=None or count < pos:
                count+=1
                if count == pos:
                    previous.setNext(currentnode.getNext())
                    self.length-=1
                    return 
                else:
                    previous = currentnode
                    currentnode = currentnode.getNext()
    
    #method for deleting singly linked list
    def clear(self):
        self.head = None





if __name__ == "__main__":
    a =Node()
    a.setData('king')

    b= Node()
    b.setData('boy')
    a.setNext(b)
    print(a.listLength(b))

