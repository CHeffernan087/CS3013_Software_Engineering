from Node import Node
class BST:
	root = None
	



	def put_recursive(self,n, key, val):

		if(n.getKey() > key):
			if(n.left==None):
				n.left = Node(key,val)
			else:
				self.put_recursive(n.left,key,val)
		elif(n.getKey() < key):
			if(n.right==None):
				n.right = Node(key,val)
			else:
				self.put_recursive(n.right,key,val)
		else:
			
			n.setValue(val)


	def put(self,key, value):
		if(self.root== None):
			self.root = Node(key,value)
			self.left=None
			self.right = None

		else:
			self.put_recursive(self.root,key,value)


 	def getRoot(self):
		return self.root


	def get(self, key):
		return self.get_recursive(self.root,key)

	def get_recursive(self, n,key):
		if(n==None):
			return None

		if(key <n.key):
			return self.get_recursive(n.left,key)
		elif(key > n.key):
			return self.get_recursive(n.right,key)	
		else:
			return n


	def printInOrder(self):
		if(self.root!=None):
			array = []
			self.printInOrderRecursive(self.root,array)
			returnString = ""
			for string in array:
				returnString+= string
			return returnString
		else:
			return ""

			
	def printInOrderRecursive(self,n,array):

		if(n==None):
			return
		self.printInOrderRecursive(n.left,array)
		n.printNode()
		array.append(n.toString()+"\n")
		self.printInOrderRecursive(n.right,array)


	def findLeftMostBranch(self,n):
		if(n.left == None):
			return n
		return self.findLeftMostBranch(n.left)

	def findMinNode(self):
		if(self.getRoot()==None):
			return None
		else:
			return self.findLeftMostBranch(self.getRoot())

	

	

	def getPathToNode(self, key):
		array = []
		if(self.get(key)==None):
			return None;
		else:
			self.recursiveGetPath(self.root,key,array)
			return array

	def recursiveGetPath(self, n, key, array):
		if(n==None):
			return 
		array.append(n)
		if(key <n.key):
			return self.recursiveGetPath(n.left,key,array)
		elif(key > n.key):
			return self.recursiveGetPath(n.right,key,array)	
		else:
			return n

	def getPathsOfNVertices(self,array):
		allPaths = []
		for key in array:
			path = self.getPathToNode(key)
			allPaths.append(path)
		return allPaths


	def printVertexPath(self,array):
			for n in array:
				n.printNode()

	def getLowestCommonAncestor(self,array):
		allPaths = self.getPathsOfNVertices(array)

		#check all nodes are in tree
		for path in allPaths:
			if(path==None):
				return None

		previousNode = None
		n = allPaths[0][0]
		i=0
		
		while i<len(allPaths[0]):

			for pathList in allPaths:
				if(pathList[i]!= n):
					return previousNode
			previousNode = n
			i = i+1
			n = allPaths[0][i]
			
		return n;



	def makeBST(self,keys,vals):
		i = 0
		for key in keys:
			self.put(key,vals[i])
			i = i+1
    	
    		

			






	


