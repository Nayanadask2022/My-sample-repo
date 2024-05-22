# Maximum value in a binary tree

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
# Returns maximum value in a
# given Binary Tree
 
 
def findMax(root):
 
    # Primary case if node is empty
    if (root == None):
        return float('-inf')
 
    # Return maximum of 3 values:
    # a) Root's data b) Max in Left Subtree
    # c) Max in right subtree
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if (lres > res):
        res = lres
    if (rres > res):
        res = rres
    return res
 
 
# Sample snippet for passing values
if __name__ == '__main__':
    root = newNode(5)
    root.left = newNode(3)
    root.right = newNode(2)
    root.left.right = newNode(11)
    root.left.left = newNode(10)
   
    # Function call
    print("Maximum element is",
          findMax(root))
