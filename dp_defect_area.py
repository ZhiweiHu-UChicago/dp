
def largestArea(samples):
    # the sample is a n*n matrix

    dp = [[0] * (len(samples[0]) + 1) for i in range(len(samples) + 1)]
    # dp matrix is a (n+1)*(n+1) zero-matrix

    max1 = 0

    for i in range(1, len(samples) + 1):
        for j in range(1, len(samples[0]) + 1):
        # iterate through the sample matrix

            if samples[i - 1][j - 1] == 1 :
            # for a given position, if in the sample matrix it's 1
            # then it's possible it could form a squared defect area
            # we just need to check its surrounding positions
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                # the tricky part: when we're sure all surrounding positions are defected
                # then the whole square is a defect square
                # the new defect square is built on the initial minimum square with side 1 unit longer
                if dp[i][j] > max1:
                    max1 = dp[i][j]
                    # update the largest square
    return max1


samples_1 = [[1,1,1,1,1],[1,1,1,0,0],[1,1,1,0,0],[1,1,1,0,0],[1,1,1,1,1]]
samples_2 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
samples_3 = [[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

print(largestArea(samples_1)) # output 3
print(largestArea(samples_2)) # output 2
print(largestArea(samples_3)) # output 4




