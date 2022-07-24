

def solve(N, K, A):
    mp = {A[0]:0}  # 出現回数を記録するのではなく、区間中の、（つまり遭遇した中で）最も右にあるidxに更新する
    r = 0
    l = 0
    max_width = 0
    while r <= N - 2:  # rがN-1になったら終わり
        # rを可能な限り右まで伸ばす
        for idx in range(r+1, N):
            if A[idx] in mp:
                mp[A[idx]] = idx
                # r = idx
            else:  # 本当はelse分いらないけど、ないと少し気持ち悪い
                mp[A[idx]] = idx
                if len(mp.keys()) > K:
                    r = idx - 1
                    break
            if idx == N-1: r = idx
        # r = idx -1 # 途中で抜けるにせよ、最後まで右端を右に動かせたとしても

        max_width = max(max_width, r-l)

        # 次にlを、区間内の文字数が減るまで動かす
        minV = N  # とりあえず大きい数字
        for k, v in mp.items():
            if v < minV:
                k_remove = k 
                minV = v
        # lをminv+1まで動かして、dictのkを除く
        # print("now :", A[l:r+1])
        # print("throw {} so that L can move to {}".format(k_remove, minV+1))
        l = minV + 1
        # print("now :", A[l:r+1])
        # print("-------------")
        mp.pop(k_remove)
    
    print(max_width+1)
    return 0




def input_args():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    return [N, K, A]

def test():
    N, K = 9, 2
    A = [2, 3, 4, 4, 3, 2, 1, 2, 3]
    return [N, K, A]

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)