


mod = 1000000007

def solve(N, B, K, digits):    
    mod = 1000000007
    dp = [[0 for _ in range(B)] for _ in range(N)]
    
    # 1桁目までで、作れる文字のうち、あまりが
    # 0, 1, ..., B-1のものが何個あるか、を書いていく
    for digit in digits:
        idx = digit % B
        dp[0][idx] += 1
    
    # DPで埋めていく
    for i in range(1, N):
        for digit in digits:  # どの文字をappendするか
            for q in range(B):  # どの余り
                idx = (q * 10 + digit) % B
                dp[i][idx] += dp[i-1][q]
                dp[i][idx] %= mod
    
    print(dp[N-1][0])
    return dp[N-1][0]


#
if __name__=="__main__":
    N, B, K = map(int, input().split())
    digits = list(map(int, input().split()))
    solve(N, B, K, digits)
