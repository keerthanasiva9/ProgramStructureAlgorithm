def num_of_islands(graph):

    rows= len(graph)
    columns= len(graph[0])
    count = 0

    for i in range(rows):
        for j in range(columns):
            if graph[i][j] == 1:
                dfs(graph,i,j)
                count = count + 1
    return count

def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
        return
    grid[i][j] = '#'
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)

if __name__ == "__main__":
    graph = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]
    print(num_of_islands( graph))