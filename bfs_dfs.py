#Name: Abhinav Rawat       Class: T.E.     Div: A          Roll No: 49
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
} 

visited= [] 
queue = []     

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:         
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

   


def dfs(visited, graph, node): 
    if node not in visited:
        print (node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)



print("1.BFS    2.DFS")
i= int(input("Enter your choice: "))
if i==1:
	print("Following is the Breadth-First Search") 
	bfs(visited, graph, '5')    

else:
	print("Following is the Depth-First Search")
	dfs(visited, graph, '5')
