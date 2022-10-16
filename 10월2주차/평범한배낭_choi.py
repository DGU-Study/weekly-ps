def knapsack(limit, wv_arr, quantity):
    dp = [[0 for _ in range(limit+1)] for _ in range(quantity+1)]
    for i in range(quantity + 1):
        for w in range(limit+1):
            if i == 0 or w==0:
                dp[i][w]==0
            elif wv_arr[i-1][0] <= w:
                dp[i][w] = max(wv_arr[i-1][1] + dp[i-1][w-wv_arr[i-1][0]], dp[i-1][w] )
            else:
                dp[i][w] =  dp[i-1][w]
    return dp[quantity][limit]

import sys

si = sys.stdin.readline

N, K = map(int, si().split())
stuff = list(list(map(int, si().split())) for _ in range(N))

print(knapsack(K, stuff, N))