def knapsack(values, weights, max_weight):
    n = len(values)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    i, w = n, max_weight
    result = []
    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:
            result.append(i-1)
            w -= weights[i-1]
        i -= 1
    return result, dp[n][max_weight]

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
res, optimized_value = knapsack(values, weights, 7)
print(optimized_value)
print(res)
