import heapq

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    def h(p):
        return abs(p[0]-goal[0]) + abs(p[1]-goal[1])
    open_set = [(h(start), 0, start)]  # (f, g, node)
    came_from = {}
    g_score = {start: 0}
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    while open_set:
        _, g, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        for d in directions:
            neighbor = (current[0]+d[0], current[1]+d[1])
            r, c = neighbor
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
                tentative_g = g + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + h(neighbor)
                    heapq.heappush(open_set, (f, tentative_g, neighbor))
    return None

if __name__ == '__main__':
    r = int(input('Rows: '))
    c = int(input('Cols: '))
    print('Enter grid rows (0=free,1=obstacle):')
    grid = [list(map(int, input().split())) for _ in range(r)]
    sr, sc = map(int, input('Start (row col): ').split())
    gr, gc = map(int, input('Goal (row col): ').split())
    path = astar(grid, (sr, sc), (gr, gc))
    if path:
        print('Path found:', path)
    else:
        print('No path')
