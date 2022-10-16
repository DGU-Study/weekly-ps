N, K = map(int, input().split())    # 물품 수, 무게
dp = [ [0] * ( K+1 ) for _ in range( N+1 )]

for i in range(1, N+1):
    weight, value = map(int, input().split())
    for j in range(1, K+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]   # 그대로 이전 항목 가져오기
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
            
print(dp[N][K])