accessible = 0

with open("input.txt", "r") as input:
    grid = [[0] * (len(input.readline()) + 1)]
with open("input.txt", "r") as input:
    for row in input.readlines():
        grid_row = [0]
        for value in row:
            if value == "@":
                grid_row.append(1)
            else:
                grid_row.append(0)
        grid_row.append(0)        
        grid.append(grid_row)
    grid.append([0 for i in grid[0]])

    row_count = len(grid)
    for y in range(1, row_count):
        column_count = len(grid[0])
        for x in range(1, column_count):
            if grid[y][x] == 1:
                values = []
                values.append(grid[y - 1][x - 1])
                values.append(grid[y - 1][x])
                values.append(grid[y - 1][x + 1])
                values.append(grid[y][x - 1])
                values.append(grid[y][x + 1])
                values.append(grid[y + 1][x - 1])
                values.append(grid[y + 1][x])
                values.append(grid[y + 1][x + 1])
                if sum(values) < 4:
                    accessible += 1
                    grid[y][x] = 0

print(accessible)