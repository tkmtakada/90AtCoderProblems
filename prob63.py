
"""
Hの選び方を全探索
"""
def solve(H, W, P):
    # bit search
    for i in range(1, 2**H):
        lst = []
        for k in range(H):
            if (i & 1<<k) == 1:
                lst.append(k)
        # 今の i の時に、1になっているi がわかった

        # 縦に同じ数字が並んでいるところがいくつあるか
        for j in range(W):
            for k in range(len(lst)):
                ... # 関数に分ければできそう

    ...



def input_args():
    H, W = map(int, input().split())
    P = []
    for _ in range(H):
        P.append(list(map(int, input().split())))
    return [H, W, P]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)