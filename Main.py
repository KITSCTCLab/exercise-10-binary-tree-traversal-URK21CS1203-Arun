class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    # Write your code here
    if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def inorder(root) -> None:
    # Write your code here
    if (root==0):
        return
    else:
        print(inorder(root.left))
        print(root.data)
        print(inorder(root.right))


def preorder(root) -> None:
    # Write your code here
    if (root==0):
        return
    else:
        print(root.data)
        print(preorder(root.left))
        print(preorder(root.right))


def postorder(root) -> None:
    # Write your code here
    if (root==0):
        return
    else:
        print(postorder(root.left))
        print(postorder(root.right))
        print(root.data)


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
