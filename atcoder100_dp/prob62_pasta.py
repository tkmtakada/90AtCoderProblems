

def solve(N, K, schedule):
    dp = [[0 for _ in range(N)] for _ in range(3)]  # 最下段は
    for date, menu in schedule:
        dp[(menu+1)%3][date] = '#'
        dp[(menu+2)%3][date] = '#'
    
    # dpを埋めていく
    # initial conditions   
    for i in range(3):
        if dp[i][0] == '#':
            dp[i][0] = 0
        else:
            dp[i][0] = 1
    
    for i in range(3):
        if dp[i][1] == '#':
            dp[i][1] = 0
        else:
            dp[i][1] = dp[0][0] + dp[1][0] + dp[2][0]

    for k in range(2,N):
        for i in range(3):
            if dp[i][k] == '#':
                dp[i][k] = 0
            elif dp[i][k-1] == 0:
                dp[i][k] = dp[0][k-1] + dp[1][k-1] + dp[2][k-1]
            else:
                dp[i][k] = dp[(i+1)%3][k-1] + dp[(i+2)%3][k-1] \
                        + dp[(i+1)%3][k-2] \
                        + dp[(i+2)%3][k-2]
            dp[i][k] %= 10000    
    print((dp[0][N-1] + dp[1][N-1] + dp[2][N-1]) % 10000)
    # print(dp)
    return 0



def input_args():
    N, K = map(int, input().split())
    schedule = []
    for _ in range(K):
        a, b = map(int, input().split())
        schedule.append([a-1,b-1])    
    return [N, K, schedule]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)