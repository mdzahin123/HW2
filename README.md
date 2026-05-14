# CMPSC 441 — Homework 2: DFS on the Penn State Harrisburg Campus

Depth-First Search (DFS) implementation that finds paths between buildings on the Penn State Harrisburg campus, modeled as a directed graph. The program finds **all** paths from a start building to a goal, then returns the **longest** one (and, for comparison, the shortest one via DFS).

**Course:** CMPSC 441 — Artificial Intelligence (Fall 2025)
**Author:** Muhammad Danish Zahin Bin Rafizal

---

## Problem

You're a new student at Penn State Harrisburg trying to get to the Madlyn L. Hanes Library. The campus is a graph of buildings connected by walkways, and the graph contains cycles, so a naive DFS would loop forever. The task is to:

1. Find every simple path from a start building to the Library.
2. Return the longest such path.
3. Handle multiple starting points (different campus entrances).
4. Track visited nodes correctly so cycles don't cause infinite recursion.

## Files

| File | Purpose |
|---|---|
| `campus_dfs.py` | DFS implementation (longest path + shortest path variant) |
| `campus_helper.py` | Provided helper — defines the graph and the `test_paths` runner. **Do not modify.** |

## Requirements

- Python 3.8+
- No external libraries

## How to Run

```bash
python campus_dfs.py
```

## The Campus Graph

The graph is a directed adjacency list returned by `get_campus_graph()`:

```
Student Enrichment Center → Olmsted Building, Science and Tech Building
Olmsted Building          → Library, Kulkarni Theatre
Science and Tech Building → Vartan Plaza, Student Enrichment Center   (cycle)
Kulkarni Theatre          → Library, Olmsted Building                 (cycle)
Vartan Plaza              → Science and Tech Building                 (cycle)
Swatara Building          → Olmsted Building
Library                   → (no outgoing edges — goal)
```

Cycles between `Student Enrichment Center ↔ Science and Tech Building`, `Olmsted Building ↔ Kulkarni Theatre`, and `Science and Tech Building ↔ Vartan Plaza` are why visited-tracking matters.

## Approach

`dfs_all_paths` is a recursive generator that yields every simple path from `start` to `goal`. The trick is that `visited` is **mutated during recursion and unmutated on backtrack**:

```python
path.append(start)
visited.add(start)
# ... recurse ...
path.pop()
visited.remove(start)   # <-- crucial
```

If we left the node marked as visited after returning, we'd block other branches from ever using it and miss valid paths. Removing it on backtrack means "visited" really means "currently on the path being explored," which is exactly what's needed to avoid cycles without losing paths.

- `dfs_longest_path` collects all paths and returns `max(..., key=len)`.
- `dfs_shortest_path` collects all paths and returns `min(..., key=len)` — included to show that DFS is **not** optimal for shortest path. BFS would do this in one sweep. DFS only finds the shortest one here because we enumerate all paths first, which is wasteful on larger graphs.

## Sample Output

```
=== Testing Longest Paths ===
Longest path from Student Enrichment Center to Library: ['Student Enrichment Center', 'Olmsted Building', 'Kulkarni Theatre', 'Library']
Longest path from Swatara Building to Library: ['Swatara Building', 'Olmsted Building', 'Kulkarni Theatre', 'Library']
Longest path from Vartan Plaza to Library: ['Vartan Plaza', 'Science and Tech Building', 'Student Enrichment Center', 'Olmsted Building', 'Kulkarni Theatre', 'Library']

=== Testing Shortest Paths (DFS-based) ===
Shortest path from Student Enrichment Center to Library: ['Student Enrichment Center', 'Olmsted Building', 'Library']
Shortest path from Swatara Building to Library: ['Swatara Building', 'Olmsted Building', 'Library']
Shortest path from Vartan Plaza to Library: ['Vartan Plaza', 'Science and Tech Building', 'Student Enrichment Center', 'Olmsted Building', 'Library']
```

## Notes & Limitations

- DFS finds *a* path quickly but doesn't minimize length — for shortest paths, BFS is the right tool. The DFS shortest-path function here works only because it enumerates every path, which is exponential in the worst case.
- "Visited" here means *on the current recursion stack*, not *ever seen*. This is what allows the algorithm to explore alternative branches that share nodes.
- The graph is directed, so `A → B` does not imply `B → A`.

## License

Submitted for coursework — not licensed for redistribution.
