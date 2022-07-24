

def solve(N, domains):
    W = 1024
    plain = [[0 for _ in range(W)] for _ in range(W)]
    for lx, ly, rx, ry in domains:
        # rx > lx, ry > ly
        plain[rx][ry] += 1
        plain[lx][ly] += 1
        plain[rx][ly] -= 1
        plain[lx][ry] -= 1
    
    # 累積していく
    for i in reversed(range(W - 1)):
        for j in reversed(range(W - 1)):
            plain[i][j] = plain[i+1][j] + plain[i][j]
    mp = {}
    for i in reversed(range(W - 1)):
        for j in reversed(range(W - 1)):
            k = plain[i][j+1] + plain[i][j]
            plain[i][j] = k
            if k in mp:
                mp[k] += 1
            elif k != 0:
                mp[k] = 1

    for i in range(1, N+1):
        print(mp[i] if i in mp else 0)
    return 0


def input_args():
    N = int(input())
    domains = []
    for _ in range(N):
        d = list(map(int, input().split()))
        domains.append(d)
    return [N, domains]

def test():
    N =  2
    domains = [[1, 1, 3, 2],
                [2, 1, 4, 2]]

    return [N, domains]

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)