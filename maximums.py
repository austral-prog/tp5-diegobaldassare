# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    # return "ANSWER HERE" # Remove this line and implement
    return x if x > y else y


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    # return "ANSWER HERE" # Remove this line and implement
    return max_of_two(max_of_two(x, y), z)