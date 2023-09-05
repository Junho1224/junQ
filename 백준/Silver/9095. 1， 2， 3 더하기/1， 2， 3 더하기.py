# 1,2,3 더하기
T = int(input())
test_cases = [int(input()) for _ in range(T)]

dp = [0, 1, 2, 4] + [0]*8 # dp[1] = 1, dp[2] = 2, dp[3] = 4

for i in range(4, 11): # 4부터 10까지
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for test_case in test_cases:
    print(dp[test_case])