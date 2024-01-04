def pascal_triangle(n):
    """
    Generate Pascal's Triangle of n rows.

    Args:
        - n: Number of rows

    Returns:
        - List of lists representing Pascal's Triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # first element in each row is always 1

        # Generate the rest of the row based on the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)  # last element in each row is always 1
        triangle.append(row)

    return triangle

# Test the implementation
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
