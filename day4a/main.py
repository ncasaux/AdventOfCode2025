import aocd

f = aocd.get_data(day=4, year=2025)

maze = []
length = len(f.splitlines()[0])
maze.append(list("#" * (length + 2)))
for line in f.splitlines():
    maze.append(list(f"#{line}#"))
maze.append(list("#" * (length + 2)))

rolls = 0

for y in range(1, len(maze) - 1):
    for x in range(1, len(maze[y]) - 1):
        if maze[y][x] == "@":
            neighbours = 0
            if maze[y - 1][x - 1] == "@": neighbours += 1
            if maze[y - 1][x] == "@": neighbours += 1
            if maze[y - 1][x + 1] == "@": neighbours += 1
            if maze[y][x - 1] == "@": neighbours += 1
            if maze[y][x + 1] == "@": neighbours += 1
            if maze[y + 1][x - 1] == "@": neighbours += 1
            if maze[y + 1][x] == "@": neighbours += 1
            if maze[y + 1][x + 1] == "@": neighbours += 1
            if neighbours < 4: rolls += 1

print(f"rolls: {rolls}")
