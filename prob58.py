

def solve(N, K):
    mp = {N:["#", 0]}
    timestamp = 1
    while True:
        digits = [int(i) for i in str(N)]
        y = sum(digits)
        prev = N
        N = (N + y) % (10**5)  # 更新
        if N in mp:
            prior = mp[N][1]
            cycle = timestamp - prior
            break
        else:
            mp[N] = ["#", timestamp]
            mp[prev][0] = N
        timestamp += 1

    # cycle決まった
    r = (K-prior) // cycle
    q = (K-prior) % cycle

    num = N
    for i in range(q):
        num = mp[num][0]
    print(num)


def input_args():
    N, K = map(int, input().split())    
    return [N, K]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)