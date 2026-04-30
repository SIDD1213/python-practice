#Count negative numbers in a sorted matrix
def countNegatives(grid):
    rows = len(grid)
    cols = len(grid[0])

    r = rows - 1
    c = 0
    count = 0

    while r >= 0 and c < cols:
        if grid[r][c] < 0:
            count += cols - c
            r -= 1
        else:
            c += 1

    return count


grid = [
    [5, 3, 1, -1],
    [4, 2, 0, -2],
    [3, 1, -1, -3],
    [1, -1, -2, -4]
]

print("Negative Numbers:", countNegatives(grid))