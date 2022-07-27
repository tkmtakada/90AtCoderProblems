
mod = 10**9 + 7

def solve(K):
    if K%9 != 0:
        print(0)
        return 0

    # dpでとく
    dp = [0 for _ in range(K+1)]
    dp[0] = 1
    for i in range(1, K+1):
        s = max(0, i-9)
        for j in range(s, i):
            dp[i] += dp[j]
        dp[i] = dp[i] % mod
    print(dp[K])
    return 0


def input_args():
    K = int(input())
    return [K]

def test():
   return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)