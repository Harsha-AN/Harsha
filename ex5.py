class Node:
    def __init__(self,data):
        self.data =data
        self.next =None

class LinkedList:
        def __init__(self):
         self.head=None

        def listprint(self):
         self.head=None

        def listprint(self):
          printval = self.head
          while printval is not None:
            print (printval.data)
            printval = printval.next


        def _inset_at_Begining(self,newdata):
            newNode =Node(newdata) 
            newNode.next =self.head
            self.head =newNode

l1 = LinkedList()
l1.head = Node("Toyota")
l2 = Node("BMW")
l3 = Node("Audi")
l4 = Node("Lambogini")
l1.head.next=l2
l1.next=l3
l1.next=l4
l1.listprint()