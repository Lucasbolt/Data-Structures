class Node:
    #if data is not given explicitly,it is assumed to be None
    def __init__(self, data=None, Next=None, prev=None):
        self.data=data
        self.next=Next
        self.prev=prev
    
    #method for setting data field of the node
    def setData(self, data):
        self.data = data
    
    #method for getting data of the node
    def getData(self):
        return self.data
    
    #method for setting the next field of the node
    def setNext(self, node):
        self.next = node

    #method for getting the next field of the node
    def getNext(self):
        return self.next

    #method for checking if the node points to another node
    def hasNext(self):
        return self.next!= None

    #method for setting the prev field for node
    def setPrev(self, prev):
        self.prev = prev

    #method for getting the prev field for the node
    def getPrev(self):
        return self.prev

    #returs True if the node points to a previous node
    def hasPrev(self):
        return self.prev != None
    
    #insert new data at the beginning of the double_linked_list
    def insertAtTheBeginning(self, data):
        newNode = Node(data, None, None)
        if self.head == None: #if there's no previous head(empty list)
            self.head = self.tail = newNode
        else:
            newNode.setPrev(None)
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode

    #insert new data at the end of a doubly_linked list
    def insertAtTheEnd(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(data, None, current))
            self.tail = current.getNext()
    
    #fetch a node in the list using index
    def getNode(self, index):
        currentNode = self.head
        if currentNode == None:
            return None
        i = 0
        while i < index and currentNode.getNext() != None:
            currentNode = currentNode.getNext()
            if currentNode.getNext() == None:
                break
        return currentNode
        
    #inserting data at a given position in  the list
    def insertInAPosition(self, index, data):
        newNode = Node(data)
        if self.head == None or index == 0:
            self.insertAtTheBeginning(data)
        elif index > 0:
            temp = self.getNode(index)
            if temp == None or temp.getNext() == None:
                self.insertAtTheEnd(data)
            else:
                newNode.setNext(temp.getNext())
                newNode.setPrev(temp)
                temp.getNext().setPrev(newNode)
                temp.setNext(newNode)

    #__str__ returns string equivalent of object
    def __str__(self):
        return "Node[Data: %s]" %(self.data)
    
    

if __name__ == "__main__":
    a = Node(data=10)
    print(a.hasPrev())
    print(a)
