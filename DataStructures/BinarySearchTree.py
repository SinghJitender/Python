class Tree:
    def __init__(self,data):
        self.right_node = None
        self.left_node = None
        self.data = data

class BST:
    def __init__(self):
        self.no_of_nodes = 0
        self.root = None

    def add(self,data):
        self.no_of_nodes+=1
        if self.root == None:
            node = Tree(data)
            self.root = node
            return
        temp = self.root
        while(temp!=None):
            if data>temp.data:
                if temp.right_node == None:
                    node = Tree(data)
                    temp.right_node = node
                    return
                temp = temp.right_node
            else:
                if temp.left_node == None:
                    node = Tree(data)
                    temp.left_node = node
                    return
                temp = temp.left_node

    def inOrderTraversal(self,node):
        temp = node
        if(temp!=None):
            print(temp.data)
            self.inOrderTraversal(temp.left_node)
            self.inOrderTraversal(temp.right_node)
            return
        return

    def __len__(self):
        return self.no_of_nodes

if __name__ == '__main__':
    t = BST()
    t.add(10)
    t.add(20)
    t.add(5)
    t.add(2)
    t.add(15)
    print(len(t))
    t.inOrderTraversal(t.root)
