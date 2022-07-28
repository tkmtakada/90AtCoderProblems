

def solve(N, L):
    dp = [0 for _ in range(N + 1)]
    dp[0] = dp[1] = 1
    for i in range(2, N+1):
        dp[i] += dp[i-1]
        if i - L >= 0: 
            dp[i] += dp[i-L]
        dp[i] = dp[i] % (10**9 + 7)
    # print("dp : ",dp)
    print(dp[N])
        



def input_args():
    N, L = map(int, input().split())
    return [N, L]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)