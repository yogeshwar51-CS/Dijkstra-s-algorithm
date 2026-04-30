from dijkstra import shortest_path

# Example graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {}
}

start = input("Enter start node: ").upper()
end = input("Enter end node: ").upper()

result = shortest_path(graph, start, end)
print(result)

print("Shortest Distance:", result[0])
print("Path:", " -> ".join(result[1]))