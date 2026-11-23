
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    w = int(input(f"Enter weight of item {i+1}: "))
    v = int(input(f"Enter value of item {i+1}: "))
    weights.append(w)
    values.append(v)

capacity = int(input("Enter knapsack capacity: "))

# Create DP table
dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for j in range(capacity + 1):

        if weights[i-1] <= j:
            dp[i][j] = max(
                values[i-1] + dp[i-1][j-weights[i-1]],
                dp[i-1][j]
            )
        else:
            dp[i][j] = dp[i-1][j]

print("Maximum Profit:", dp[n][capacity])
