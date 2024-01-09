#!/usr/bin/python3
"""
Module with a method that determines if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    - boxes (list of lists): Each box is numbered sequentially from 0 to n - 1
      and may contain keys to other boxes.

    Returns:
    - True if all boxes can be opened, else False.
    """

    # List to keep track of opened boxes
    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True  # The first box is unlocked by default

    # Stack to keep track of keys and boxes to explore
    stack = [0]  # Start with the first box

    # DFS traversal to check if all boxes can be opened
    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not opened_boxes[key]:
                opened_boxes[key] = True
                stack.append(key)

    # Check if all boxes are opened
    return all(opened_boxes)


# Example usage as provided in the task
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
