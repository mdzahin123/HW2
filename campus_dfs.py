
# campus_dfs.py
# Homework 2 
# Author: Muhammmad Danish Zahin Bin Rafizal
# Date: 10/3/2025

from campus_helper import get_campus_graph, test_paths

def dfs_all_paths(graph, start, goal, path=None, visited=None):
    """Recursive DFS to find all paths from start to goal."""
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    # If goal reached, yield the path
    if start == goal:
        yield list(path)
    else:
        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                yield from dfs_all_paths(graph, neighbor, goal, path, visited)

    # Backtrack
    path.pop()
    visited.remove(start)

def dfs_longest_path(graph, start, goal):
    """Return the longest path from start to goal using DFS backtracking."""
    all_paths = list(dfs_all_paths(graph, start, goal))
    if not all_paths:
        return None
    # Return the longest path (if tie, any one is fine)
    return max(all_paths, key=len)

def dfs_shortest_path(graph, start, goal):
    all_paths = list(dfs_all_paths(graph, start, goal))
    if not all_paths:
        return None
    return min(all_paths, key=len)

if __name__ == "__main__":
    graph = get_campus_graph()

    print("=== Testing Longest Paths ===")
    test_paths(dfs_longest_path)

    print("\n=== Testing Shortest Paths (DFS-based) ===")
    for start, goal in [
        ('Student Enrichment Center', 'Library'),
        ('Swatara Building', 'Library'),
        ('Vartan Plaza', 'Library')
    ]:
        print(f"Shortest path from {start} to {goal}: {dfs_shortest_path(graph, start, goal)}")



