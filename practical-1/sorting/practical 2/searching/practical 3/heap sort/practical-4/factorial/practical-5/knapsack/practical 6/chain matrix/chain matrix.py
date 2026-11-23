
# Matrix Chain Multiplication

n = int(input("Enter number of matrices: "))

p = list(map(int, input("Enter dimensions: ").split()))

dp = [[0] * n for _ in range(n)]

# Chain length
for L in range(2, n + 1):
    for i in range(n - L + 1):
        j = i + L - 1
        dp[i][j] = float('inf')

        for k in range(i, j):
            cost = (dp[i][k] + dp[k+1][j]
                    + p[i] * p[k+1] * p[j+1])

            dp[i][j] = min(dp[i][j], cost)

print("Minimum number of multiplications:", dp[0][n-1])
