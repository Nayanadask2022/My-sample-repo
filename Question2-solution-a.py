# A class to create a new node
  
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
    # 1) Root's data 2) Max in Left Subtree
    # 3) Max in right subtree
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if (lres > res):
        res = lres
    if (rres > res):
        res = rres
    return res
 
 
# Sample program for passing values
if __name__ == '__main__':
    root = newNode(5)
    root.left = newNode(3)
    root.right = newNode(2)
    root.left.right = newNode(11)
    root.left.left = newNode(10)
   
    # Function call
    print("Maximum element is",
          findMax(root))
