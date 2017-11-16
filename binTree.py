'''
@author: Mirav Gokani
'''

# Practicing binary search tree algorithms

class TreeNode():
    # Constructor to initialize attributes of the class
    def __init__(self, key, leftChild, rightChild, parent):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent


class BinSearchTree():
    # Constructor to initialize attributes of the class
    def __init__(self):
        self.root = None
        self.sum = 0
        self.array = []

    # Returns root of the binary tree
    def returnRoot(self):
        return self.root.key

    # Add child nodes to the binary tree
    def addChild(self, key, Node):
        if (key < Node.key):
            if (Node.leftChild != None):
                self.addChild(key, Node.leftChild)
            else:
                Node.leftChild = TreeNode(key, None, None, Node)
        else:
            if (Node.rightChild != None):
                self.addChild(key, Node.rightChild)
            else:
                Node.rightChild = TreeNode(key, None, None, Node)

    # Add nodes to the binary tree
    def addNode(self, key):
        if self.root == None:
            self.root = TreeNode(key, None, None, None)
        else:
            self.addChild(key, self.root)

    # Performs inOrder tree walk
    def inorderTreeWalk(self, Node):
        if Node != None:
            self.inorderTreeWalk(Node.leftChild)
            print(Node.key)
            self.inorderTreeWalk(Node.rightChild)

    # Performs preOrder tree walk
    def preOrderTreeWalk(self, Node):
        if Node != None:
            print(Node.key)
            self.preOrderTreeWalk(Node.leftChild)
            self.preOrderTreeWalk(Node.rightChild)

    # Performs postOrder tree walk
    def postOrderTreeWalk(self, Node):
        if Node != None:
            self.postOrderTreeWalk(Node.leftChild)
            self.postOrderTreeWalk(Node.rightChild)
            print(Node.key)

    # Searches an element in the tree and returns the path from root to the element
    def modifiedTreeSearch(self, Node, key):
        if (Node == None):
            return Node
        elif (key == Node.key):
            self.array.append(Node.key)
            return Node
        elif key < Node.key:
            self.array.append(Node.key)
            return self.modifiedTreeSearch(Node.leftChild, key)
        else:
            self.array.append(Node.key)
            return self.modifiedTreeSearch(Node.rightChild, key)

    # Finds minimum element in the tree
    def TreeMinimum(self, Node):
        while Node.leftChild != None:
            Node = Node.leftChild
        return Node

    # Finds maximum element in the tree
    def TreeMaximum(self, Node):
        while Node.rightChild != None:
            Node = Node.rightChild
        return Node

    # Finds successor of an element
    def TreeSuccessor(self, Node):
        if Node.rightChild != None:
            return self.TreeMinimum(Node.rightChild)
        parentNode = Node.parent
        while parentNode != None and Node == parentNode.rightChild:
            Node = parentNode
            parentNode = parentNode.parent
        return parentNode

    # Finds predecessor of an element
    def TreePredeccessor(self, Node):
        if Node.leftChild != None:
            return self.TreeMaximum(Node.leftChild)
        parentNode = Node.parent
        while parentNode != None and Node == parentNode.leftChild:
            Node = parentNode
            parentNode = parentNode.parent
        return parentNode

    # Insert an element to the binary tree
    def TreeInsert(self, T, Node):
        p = Node.parent
        x = T.root
        while x != None:
            p = x
            if Node.key < x.key:
                x = x.leftChild
            else:
                x = x.rightChild
        Node.parent = p
        if p == None:
            T.root = Node  # Tree was empty
        elif Node.key < p.key:
            p.leftChild = Node
        else:
            p.rightChild = Node

    # Calculates height of the tree
    def height(self, Node):
        if Node == None:
            # Height of root node  = 0
            return -1
        else:
            return max(self.height(Node.leftChild), self.height(Node.rightChild)) + 1

    # Calculates sum of leaf nodes
    def sumofleafNodes(self, Node):
        if Node == None:
            return 0
        if Node.leftChild == None and Node.rightChild == None:
            self.sum += Node.key
        else:
            self.sumofleafNodes(Node.leftChild)
            self.sumofleafNodes(Node.rightChild)
        return self.sum


def main():
    bt = BinSearchTree()
    data = [5, 4, 10, 3, 11, 12, 6, 7, 2, 1, 20, 8]
    data = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]

    for val in data:
        bt.addNode(val)

    print("Root =", bt.returnRoot())
    print("Height of the tree =", bt.height(bt.root))
    print("Printing elements after inOrder tree walk")
    bt.inorderTreeWalk(bt.root)
    print("Printing elements after preOrder tree walk")
    bt.preOrderTreeWalk(bt.root)
    print("Printing elements after postOrder tree walk")
    bt.postOrderTreeWalk(bt.root)
    print("Minimum element =", bt.TreeMinimum(bt.root).key)
    print("Maximum element =", bt.TreeMaximum(bt.root).key)
    print("Sum of leaf nodes =", bt.sumofleafNodes(bt.root))

    node = bt.modifiedTreeSearch(bt.root, 13)

    if node == None:
        print("Element not found")
    else:
        print("Printing all keys in the path from root to searched element")
        for i in bt.array: print(i)
        print("Successor of the searched element =", bt.TreeSuccessor(node).key)
        print("Predeccessor of the searched element =", bt.TreePredeccessor(node).key)


    tn=TreeNode(8, None, None, None)
    bt.TreeInsert(bt, tn)
    print("Printing inOrder tree walk elements after node insertion")
    bt.inorderTreeWalk(bt.root)
    print("Height after node insertion =", bt.height(bt.root))


if __name__ == "__main__":
    main()