from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print('found it')
            return self

        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print("value is not in tree")

    def height(self, h=0):
        left_height = self.left.height(h+1) if self.left else h
        right_height = self.right.height(h+1) if self.right else h
        return max(left_height, right_height)

    def traversePreorder(self):

        print(self.data)
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()

    def traverseInorder(self):

        if self.left:
            self.left.traversePreorder()
        print(self.data)
        if self.right:
            self.right.traversePreorder()

    def traversePostorder(self):

        if self.left:
            self.left.traversePreorder()

        if self.right:
            self.right.traversePreorder()
        print(self.data)

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.search(target)

    def traversePreorder(self):
        self.root.traversePreorder()

    def traverseInorder(self):
        self.root.traverseInorder()

    def traversePostorder(self):
        self.root.traversePostorder()

    def height(self):
        return self.root.height()





# node = Node(10)
#
# node.left = Node(5)
# node.right = Node(15)
#
# node.left.left = Node(2)
# node.right.right = Node(6)
#
# node.right.left = Node(13)
# node.right.right = Node(10000)
#
# print(node.right.data)
# print(node.right.right.data)
#
# myTree = Tree(node, 'Ryan_stree')
#
# print(myTree.name)
# print(myTree.root.right.right.data)
#
#
# found = myTree.root.search(10000)


tree = Tree(Node(50), 'Tree traversals')

tree.root.left= Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left= Node(30)
tree.root.left.right.right= Node(42)
tree.root.left.left.left= Node(5)
tree.root.left.left.right= Node(13)
tree.root.left.left.left.left = Node(2)

print("traverse PRE-order")
tree.traversePreorder()

print("\ntraverse IN-order")
tree.traverseInorder()

print("\ntraverse POST-order")
tree.traversePreorder()


print("\n",'\n' )
print("tree height is:")
print(tree.root.height())