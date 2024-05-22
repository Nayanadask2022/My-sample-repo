# Depth of binary tree


class Node:

	# Constructor 
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Compute the "maxDepth" of a tree 


def maxDepth(node):
	if node is None:
		return 0

	else:

		# Compute the depth of each subtree
		lDepth = maxDepth(node.left)
		rDepth = maxDepth(node.right)

		# Using the larger one
		if (lDepth > rDepth):
			return lDepth+1
		else:
			return rDepth+1


# Sample program to test above function
root = Node(5)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(10)
root.left.right = Node(11)


print("Height of tree is %d" % (maxDepth(root)))

