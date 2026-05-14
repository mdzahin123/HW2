# Assignment 1
# Do not modify any code in this file.

def get_campus_graph():
    """Returns the campus graph as an adjacency list."""
    return {
        'Student Enrichment Center': ['Olmsted Building', 'Science and Tech Building'],
        'Olmsted Building': ['Library', 'Kulkarni Theatre'],
        'Science and Tech Building': ['Vartan Plaza', 'Student Enrichment Center'],  # Added cycle for challenge
        'Kulkarni Theatre': ['Library', 'Olmsted Building'],  # Added cycle
        'Vartan Plaza': ['Science and Tech Building'],  # Cycle potential
        'Library': [],
        'Swatara Building': ['Olmsted Building']  # Additional start point for testing
    }

def test_paths(dfs_func):
    """Tests the DFS function with multiple start-goal pairs."""
    graph = get_campus_graph()
    tests = [
        ('Student Enrichment Center', 'Library'),
        ('Swatara Building', 'Library'),
        ('Vartan Plaza', 'Library')  # Potential dead-end or cycle test
    ]
    for start, goal in tests:
        path = dfs_func(graph, start, goal)
        print(f"Longest path from {start} to {goal}: {path}")