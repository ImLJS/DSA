# Q. Island Count

# Given a 2D array binaryMatrix of W's and L's (W representing water and L representing land),
# return the number of islands in binaryMatrix.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.


def dfs(matrix, row, col, visited):  # Depth First Search
    if (  # if row or col is out of bounds or if the cell is water
        not 0 <= row < len(matrix)
        or not 0 <= col < len(matrix[0])
        or matrix[row][col] == "W"
    ):
        return False
    if (row, col) in visited:  # if the cell has already been visited
        return False
    visited.add((row, col))
    dfs(matrix, row + 1, col, visited)  # recursively call dfs on all 4 directions
    dfs(matrix, row - 1, col, visited)
    dfs(matrix, row, col + 1, visited)
    dfs(matrix, row, col - 1, visited)
    return True


def island_count(
    matrix,
):  # O(n*m) time | O(n*m) space where n is the number of rows and m is the number of columns
    count = 0
    visited = set()  # set to keep track of visited cells

    rows = len(matrix)  # get the number of rows and columns
    cols = len(matrix[0])

    for r in range(rows):  # iterate through the matrix
        for c in range(cols):
            if matrix[r][c] == "L":  # if the cell is land and has not been visited
                if dfs(matrix, r, c, visited):  # call dfs on the cell
                    count += 1  # if dfs returns True, increment the count

    return count  # return the count of islands


grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]

grid2 = [
    ["L", "W", "W", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["W", "L", "W", "L", "W"],
    ["W", "W", "W", "W", "W"],
    ["W", "W", "L", "L", "L"],
]

grid3 = [
    ["L", "L", "L"],
    ["L", "L", "L"],
    ["L", "L", "L"],
]

grid4 = [
    ["W", "W"],
    ["W", "W"],
    ["W", "W"],
]
print(island_count(grid))  # 3
print(island_count(grid2))  # 4
print(island_count(grid3))  # 1
print(island_count(grid4))  # 0
