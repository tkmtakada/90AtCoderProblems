def isSplitable(A, L, K, mid):
    # A = A + [L]
    start = 0
    counter = 0
    for i in range(len(A)):
        """
        L - A[i]の条件をつければ、明快なことに気づかなかった
        """
        if A[i] - start >= mid and L - A[i] >= mid:
            # print("lenght is ", A[i]- start)
            start = A[i]
            counter += 1
    # counterがちょうどKでも、
    return bool(counter >= K)

def solve(N, L, K, A):
    left = 1
    right = (L // K+1 ) + 1
    mid = (right + left) // 2
    # isSplitableList = [0] * 

    """
    終了条件で、幅1になった時点で終了すること
    left, rightの更新条件に、+-1をつけないこと
    これができなかった。
    """
    while (right - left) > 1:
        mid = (right + left) // 2
        # Trueなら、大きくしていい
        #　Falseなら小さくする
        # print("current mid", mid)
        if isSplitable(A, L, K, mid):
            # print("true")
            left = mid
        else:
            # print("false")
            right = mid
    
    print(left)
    # return mid




#
if __name__=="__main__":
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))
    # N, L = 3, 34
    # K = 1
    # A = [8,13,26]
    solve(N, L, K, A)
