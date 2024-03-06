#!/usr/bin/python3
"""
Function to calculate the perimeter of an island described in grid.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid (list of list of int): The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """

    perimeter = 0

    # Define directions to check surrounding cells (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # If cell is land
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                        perimeter += 1

    return perimeter


# Example usage
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
