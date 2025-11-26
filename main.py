import heapq

def dijkstra_shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return [], None
    if start == goal:
        return [start], 0

    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    parent = {}
    heap = [(0, start)]

    while heap:
        current_dist, node = heapq.heappop(heap)
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                parent[neighbor] = node
                heapq.heappush(heap, (dist[neighbor], neighbor))

    if goal not in parent and start != goal:
        return [], None

    # Reconstruct path
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path, dist[goal]


if __name__ == "__main__":
    # Demo graph matching the test file weights exactly
    sample_graph = {
        "Start": [("A", 2), ("B", 5)],
        "A": [("Start", 2), ("C", 1)],
        "B": [("Start", 5), ("C", 3), ("D", 7)],
        "C": [("A", 1), ("B", 3), ("End", 2)],
        "D": [("B", 7), ("End", 1)],
        "End": [("C", 2), ("D", 1)],
    }
    path, cost = dijkstra_shortest_path(sample_graph, "Start", "End")
    print("Sample path from Start to End:", path, "cost:", cost)
