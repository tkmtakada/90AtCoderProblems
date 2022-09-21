

def solve(n):
    dp = [1] * (n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    print(dp[n])
    return 



def input_args():
    n = int(input())
    return [n]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)