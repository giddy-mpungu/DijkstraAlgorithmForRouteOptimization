# Python program for Dijkstra's
# single source shortest
# path algorithm. The program
# is for adjacency matrix
# representation of the graph

from collections import defaultdict

#Class to represent a graph
class Graph:

	# A utility function to find the
	# vertex with minimum dist value, from
	# the set of vertices still in queue
	def minDistance(self,dist,queue):
		# Initialize min value and min_index as -1
		minimum = float("Inf")
		min_index = -1

		# from the dist array,pick one which
		# has min value and is till in queue
		for i in range(len(dist)):
			if dist[i] < minimum and i in queue:
				minimum = dist[i]
				min_index = i
		return min_index


	# Function to print shortest path
	# from source to j
	# using parent array
	def printPath(self, parent, j):

		#Base Case : If j is source
		if parent[j] == -1 :
			print (j),
			return
		self.printPath(parent , parent[j])
		print (j),


	# A utility function to print
	# the constructed distance
	# array
	def printSolution(self, dist, parent):
		src = 0
		print("Vertex \t\tDistance from Source\tPath")
		for i in range(1, len(dist)):
			print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])),
			self.printPath(parent,i)


	'''Function that implements Dijkstra's single source shortest path
	algorithm for a graph represented using adjacency matrix
	representation'''
	def dijkstra(self, graph, src):

		row = len(graph)
		col = len(graph[0])

		# The output array. dist[i] will hold
		# the shortest distance from src to i
		# Initialize all distances as INFINITE
		dist = [float("Inf")] * row

		#Parent array to store
		# shortest path tree
		parent = [-1] * row

		# Distance of source vertex
		# from itself is always 0
		dist[src] = 0

		# Add all vertices in queue
		queue = []
		for i in range(row):
			queue.append(i)

		#Find shortest path for all vertices
		while queue:

			# Pick the minimum dist vertex
			# from the set of vertices
			# still in queue
			u = self.minDistance(dist,queue)

			# remove min element
			queue.remove(u)

			# Update dist value and parent
			# index of the adjacent vertices of
			# the picked vertex. Consider only
			# those vertices which are still in
			# queue
			for i in range(col):
				'''Update dist[i] only if it is in queue, there is
				an edge from u to i, and total weight of path from
				src to i through u is smaller than current value of
				dist[i]'''
				if graph[u][i] and i in queue:
					if dist[u] + graph[u][i] < dist[i]:
						dist[i] = dist[u] + graph[u][i]
						parent[i] = u


		# print the constructed distance array
		self.printSolution(dist,parent)

g= Graph()

graph = [[0, 481, 527, 379, 396, 0, 0, 0, 0, 0],
		[481, 0, 0, 0, 793, 0, 0, 992, 0, 0],
		[527, 0, 0, 229, 0, 0, 0, 616, 1123, 0],
		[379, 0, 229, 0, 480, 431, 0, 0, 0, 0],
		[396, 793, 0, 480, 0, 1126, 0, 0, 0, 1294],
		[0, 0, 0, 431, 1126, 0, 0, 0, 741, 969],
		[0, 0, 0, 0, 0, 0, 0, 1025, 754, 1473],
		[0, 992, 616, 0, 0, 0, 1025, 0, 0, 0],
		[0, 0, 1123, 0, 0, 741, 754, 0, 0, 1100],
		[0, 0, 0, 0, 1294, 969, 1473, 0, 1100, 0]
		]

# Print the solution
g.dijkstra(graph,0)
