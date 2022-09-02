

def solve(N, K):
    n = K * (K-1)
    for i in range(2, N):
        n *= (K - 2)
        n = n % (10**9 + 7) 
    print(n)
    return 



def input_args():
    N, K = map(int, input().split())
    return [N, K]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)