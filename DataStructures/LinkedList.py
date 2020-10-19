from DataStructures.Node import Node

class LinkedList:
    def __init__(self):
        self.no_of_nodes = 0
        self.head = None

    def add(self,data):
        self.no_of_nodes+=1
        if self.head == None:
            node = Node(data)
            node.node_next = None
            self.head = node
        else:
            node = Node(data)
            node.node_next = self.head
            self.head = node

    def traverse(self):
        temp = self.head
        while temp != None:
            print(temp.data,sep=" ")
            temp = temp.node_next

    def search(self,data):
        temp = self.head
        flag = False
        index = 0
        while temp.node_next !=None:
            if(temp.data == data):
                flag = True
                break
            temp = temp.node_next
            index+=1
        if flag:
            print(f"Element {data} Found at index : {index}")
        else:
            print(f"Element Not Found")

    def remove(self,data):
        if self.head.data == data:
            self.head = self.head.node_next
            self.no_of_nodes -= 1
            print(f"Element {data} Removed")
            return
        temp = self.head
        while(temp!=None):
            if (temp.node_next.data == data):
                temp.node_next = temp.node_next.node_next
                self.no_of_nodes -= 1
                print(f"Element {data} Removed")
                return
            temp = temp.node_next
        print(f"Element {data} Not Found")
        return

    def __len__(self):
        return self.no_of_nodes

if __name__ == '__main__':
    ll = LinkedList()
    ll.add(20)
    ll.add(35)
    ll.add(12)
    ll.add(19)
    ll.add(78)
    print("----------")
    print(f"Length - {len(ll)}")
    print("----------")
    ll.traverse()
    print("----------")
    ll.search(35)
    print("----------")
    ll.search(99)
    print("----------")
    ll.remove(78)
    print("----------")
    ll.traverse()
    print("----------")
    ll.add(78)
    ll.traverse()
    print("----------")
    print(f"Length - {len(ll)}")
    ll.remove(12)
    print(f"Length - {len(ll)}")
    print("----------")
    ll.traverse()
    ll.remove(20)
    print("----------")
    ll.traverse()
    print(f"Length - {len(ll)}")