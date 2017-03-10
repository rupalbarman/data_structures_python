'''
	Binary Searc Tree Simple

	Rupal Barman
	rupalbarman@gmail.com

'''
class Node(object):
	count=0
	def __init__(self, data, left= None, right= None):
		self.data= data
		self.left= left
		self.right= right
		Node.count+=1

class Tree(object):
	def __init__(self):
		self.root= None

	def insert(self, data):
		if self.root==None:
			self.root= Node(data)
		else:
			curr= self.root
			while True:
				if data< curr.data:
					if curr.left:
						curr= curr.left
					else:
						curr.left= Node(data)
						break

				elif data> curr.data:
					if curr.right:
						curr= curr.right
					else:
						curr.right= Node(data)
						break

	def inorder(self, node):
		if node!=None:
			self.inorder(node.left)
			print(node.data)
			self.inorder(node.right)





