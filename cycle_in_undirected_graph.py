graph = [[1, 2], [0, 2], [0, 1]]

def cycleUtil(graph, visited, node, parent):
	visited[node] = True

	for i in graph[node]:
		if visited[i] == False:
			if cycleUtil(graph, visited, i, node) == True:
				return True
		elif parent != i:
			return True

	return False


def cycle(graph):
	visited = [False for i in range(len(graph))]
	
	for node in range(len(graph)):
		if visited[node] == False:
			if cycleUtil(graph, visited, node, -1) == True:
				return True

	return False

print(cycle(graph))