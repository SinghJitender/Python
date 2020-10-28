class Tree:
    def __init__(self,data):
        self.right_node = None
        self.left_node = None
        self.data = data
        self.parent = None

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
                    node.parent = temp
                    temp.right_node = node
                    return
                temp = temp.right_node
            else:
                if temp.left_node == None:
                    node = Tree(data)
                    node.parent = temp
                    temp.left_node = node
                    return
                temp = temp.left_node

    def search(self,data):
        temp = self.root
        while(temp!=None):
            if temp.data==data:
                return f"{data} Found"
            if temp.data>=data:
                temp = temp.left_node
            else:
                temp = temp.right_node
        return f"{data} Not Found"

    def delete(self,data,node,parent):
        if(self.root == None):
            return
        #Case When Node to be deleted is leaf node:
        if(node.data==data and node.left_node == None and node.right_node == None):
            if node.parent.data>data:
                node.parent.right_node = None
                del node
                return
            else:
                node.parent.left_node = None
                del node
                return
        #Case when left node is not None and right node is none of the node to be deleted
        if(node.data==data and node.left_node != None and node.right_node == None):
            if node.parent.data > data:
                node.parent.right_node = node.left_node
                del node
                return
            else:
                node.parent.left_node = node.left_node
                del node
                return

        #Case when left node is None and right node is not none of the node to be deleted
        if(node.data==data and node.left_node == None and node.right_node != None):
            if node.parent.data > data:
                node.parent.right_node = node.right_node
                del node
                return
            else:
                node.parent.left_node = node.right_node
                del node
                return

        #Case when both the nodes are not None
        if(node.data==data and node.left_node != None and node.right_node != None):
            temp = node.left_node
            while(temp.right_node!=None):
                temp = temp.right_node
            node.data = temp.data
            del temp
            return

        if(data>node.data):
            self.delete(data,node.right_node,node)
        else:
            self.delete(data,node.left_node,node)


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
    print("---------")
    t.inOrderTraversal(t.root)
    print("---------")
    print(t.search(15))
    t.add(15)
    print("---------")
    t.inOrderTraversal(t.root)
    print("---------")
    print(t.search(15))
    print("---------")
    print(t.search(10))
    print("---------")
    print(f"No of nodes : {len(t)}")
    print("---------")

