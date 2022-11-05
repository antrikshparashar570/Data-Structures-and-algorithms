d = {
		0: [2, 3],
		1: [],
		2: [],
		3: [1],
		4: [1, 2],
		5: [0, 2]
}


def dfs(d, v, visited, stack):
	visited[v] = True
	for i in d[v]:
		if not visited[i]:
			dfs(d, i, visited, stack)
	stack.append(v)
	
def topoSort(d):
	stack = []
	visited = [False for i in range(len(d))]
	for key in d.keys():
		if not visited[key]:
			dfs(d, key, visited, stack)
	print(stack[::-1])
	
topoSort(d)
		
