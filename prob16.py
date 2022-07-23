

def solve(N, A, B, C):
    dp = [float('inf') for _ in range(N+1)] 
    dp[A] = dp[B] = dp[C] = 1
    lst = [A, B, C]
    lst.sort()
    A, B, C = lst[0], lst[1], lst[2]
    for i in range(A+1, N+1):
        dp[i] = min(dp[i - A], dp[i-B], dp[i-C]) + 1
    
    print(dp[N])


def solve2(N, A, B, C):
    ans = float('inf')
    for i in range(9999):
        for j in range(9999 - i):
            v = N - i * A - j * B
            r = i + j + v / C
            if (v % C != 0) or v < 0 or r > 9999:
                continue
            ans = min(ans, r)
    print(ans)

def input_args():
    N = int(input())
    A, B, C = map(int, input().split())
    return [N, A, B, C]

def test():
   return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve2(*args)