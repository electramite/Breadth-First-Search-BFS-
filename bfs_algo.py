
adj_list = {
	"A": ["B", "D"],  # adjacency list
	"B": ["A", "C"],
	"C": ["B"],
	"D": ["A", "E", "F"],
	"E": ["D", "F", "G"],
	"F": ["D", "E", "H"],
	"G": ["E", "H"],
	"H": ["G", "F"],
}
# adj_list = {
# 	"A": ["B", "D", "E"],
# 	"B": ["A", "C", "G"],
# 	"C": ["B"],
# 	"D": ["A", "E"],
# 	"E": ["A", "F", "H", "D"],
# 	"F": ["E"],
# 	"G": ["B"],
# 	"H": ["E"],
# }

visited = {}
level = {}
parent = {}
bfs_traversal_output = []

for node in adj_list.keys():
	visited[node] = False
	parent[node] = None
	level[node] = -1

start = "A"
visited[start] = True
level[start] = 0
l = []
l.append(start)

while len(l)>0:
	u = l.pop(0)
	bfs_traversal_output.append(u)
	for v in adj_list[u]:
		if not visited[v]:
			visited[v] = True
			parent[v] = u
			level[v] = level[u] + 1
			l.append(v)

endPoint = "G"
path = []
print(parent)
while endPoint is not None:
	path.append(endPoint)
	endPoint = parent[endPoint]
path.reverse()

print(bfs_traversal_output)
print(level)
print(parent)
print(path)
