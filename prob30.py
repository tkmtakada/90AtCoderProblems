

def solve(N, K):
    # エラトステネス的な素数判定をする
    c = [0 for _ in range(N+1)]
    for i in range(2, N+1):
        if c[i] == 0:  # iは素数
            for j in range(i, N+1, i):
                c[j] += 1
        else:  # iは素数じゃない
            pass
    gtk = 0
    for i in range(len(c)):
        if c[i] >= K:
            # print(i)
            gtk += 1
    print(gtk)
    return 0


def input_args():
    N, K = map(int, input().split())
    return [N, K]

def test():
    return [15,2]

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)