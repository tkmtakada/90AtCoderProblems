

def solve(N, A):
    # dp = [[float('inf') for _ in range(2*N)] for _ in range(2*N)]
    dp = [["#" for _ in range(2*N)] for _ in range(2*N)]


    # 初期値
    for i in range(2*N-1):
        dp[i][i+1] = abs(A[i] - A[i+1])

    # dpで埋めていく
    for i in range(2, N+1):
        diff = 2 * i -1
        for j in range(2*N - diff):
            dp[j][j+diff] = getDP(j, j+diff, A, dp)
    print(dp[0][2*N-1])
    return 0

def getDP(l, r, A, dp):    
    minCost = dp[l+1][r-1] + abs(A[l] - A[r])
    for k in range(l+1, r-1, 2):
        cost = dp[l][k] + dp[k+1][r]
        minCost = min(cost, minCost)
    return minCost



def input_args():
    N = int(input())
    A = list(map(int, input().split()))
    return [N, A]

def test():
    N = 4
    A = [1, 2, 4, 8, 16, 32, 64, 128]
    return [N, A]

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)