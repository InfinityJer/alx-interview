#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing the data set.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    # Initialize a variable to track the number of expected following bytes
    expected_following_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte (starts with '10')
        if expected_following_bytes > 0:
            if (byte >> 6) == 0b10:
                expected_following_bytes -= 1
            else:
                return False
        else:
            # Checks number of leading to determine number of following bytes
            if (byte >> 7) == 0b0:
                # Single-byte character
                continue
            elif (byte >> 5) == 0b110:
                # Two-byte character
                expected_following_bytes = 1
            elif (byte >> 4) == 0b1110:
                # Three-byte character
                expected_following_bytes = 2
            elif (byte >> 3) == 0b11110:
                # Four-byte character
                expected_following_bytes = 3
            else:
                return False

    # Check if all expected following bytes are present
    return expected_following_bytes == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115,
            32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
