import heapq
import numpy as np

def heuristic(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_neighbors(node, shape):
    neighbors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = node[0] + dx, node[1] + dy
        if 0 <= nx < shape[0] and 0 <= ny < shape[1]:
            neighbors.append((nx, ny))
    return neighbors

def find_path(grid, start, goal):
    """a* implementation"""
    q = []
    heapq.heappush(q, (0, start))
    parent = {}
    g_map = {start: 0}
    while q:
        _, curr = heapq.heappop(q)
        if curr == goal:
            res = []
            while curr in parent:
                res.append(curr)
                curr = parent[curr]
            res.append(start)
            return res[::-1]
        for nxt in get_neighbors(curr, grid.shape):
            val = grid[nxt[0], nxt[1]]
            if np.isinf(val):
                continue
            tmp_g = g_map[curr] + val
            if tmp_g < g_map.get(nxt, float('inf')):
                parent[nxt] = curr
                g_map[nxt] = tmp_g
                f = tmp_g + heuristic(nxt, goal)
                heapq.heappush(q, (f, nxt))
    return None
