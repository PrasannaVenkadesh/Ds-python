#Graph Data Structure in Python
'''
A vertex 'v1' is said to be adjacent to vertex 'v2' if there exist an Edge 'e' in between them.
There are 2 ways of implementing a graph in Python. 
1. Adjacency matrix.
2. Adjacency List.

In this program let us take the 2nd approach (Adjacency List) to implement graph.
'''

#Vertex class which has payloads about individual vertices
class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}

	def addNeighbour(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def __str__(self):
		return str(self.id) +' connectedTo : ' + str([x.id for x in self.connectedTo])

	def getConnection(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self, nbr):
		return self.connectedTo[nbr]

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self, key):
		self.numVertices += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self, n):
		if n in self.vertList:
			return self.vertList[n]

	def __contains__(self, n):
		return n in self.vertList

	def addEdge(self, f, t, cost=0):
		if f not in self.vertList:
			self.addVertex(f)
		if t not in self.vertList:
			self.addVertex(t)
		self.vertList[f].addNeighbour(self.vertList[t], cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())