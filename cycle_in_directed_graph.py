graph = [[1, 2], [], [1]]

def cycleUtil(graph, visited, recstack, node):
	visited[node] = True
	recstack[node] = True

	for i in graph[node]:
		if visited[i] == False:
			if cycleUtil(graph, visited, recstack, i) == True:
				return True
		elif recstack[i] == True:
			return True

	recstack[node] = False
	return False


def cycle(graph):
	visited = [False for i in range(len(graph))]
	recstack = [False for i in range(len(graph))]
	
	for node in range(len(graph)):
		if visited[node] == False:
			if cycleUtil(graph, visited, recstack, node) == True:
				return True

	return False

print(cycle(graph))