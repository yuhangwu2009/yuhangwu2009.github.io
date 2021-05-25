def path_finder(maze):
    maze = "\n".split(maze)
    for i in maze:
        maze[i] = list(maze[i])
    return maze

maze = input()
print(maze)
print(path_finder(maze))
