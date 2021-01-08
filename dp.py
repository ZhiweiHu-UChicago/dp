# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY magic
#  2. INTEGER_ARRAY dist
#

def optimalPoint(magic, dist):
    # Write your code here
    optimal_index = 0
    surplus_magic = 0
    deficit_magic = 0

    for i, val in enumerate(magic):
        surplus_magic = surplus_magic + val - dist[i]
        if surplus_magic < 0:
            optimal_index = i + 1
            deficit_magic = deficit_magic + surplus_magic
            surplus_magic = 0

    if surplus_magic + deficit_magic >= 0:
        return optimal_index
    else:
        return -1
