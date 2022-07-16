
def solve(N, A, Q, B):
    """
    Aをソートして
    Qをbinary search
    """
    # そーと
    A.sort()

    # binary search
    ans = []
    for b in B:
        s = 0
        e = N-1
        # m = (s + e) // 2

        foundB = False
        while e - s > 1:
            m = (s + e) // 2

            if A[m] == b:
                ans.append(0)
                foundB = True
                break
            elif A[m] < b:
                s = m
            elif b < A[m]:
                e = m
        # whileぶんが終わったとき、
        # 状況は2つありえる
        #  1. すでにmがansにappendされてる
        # 2. sとeのあいだに
        if not foundB:
            ans.append(min(abs(A[s] - b), abs(A[e] - b)))
    # print(ans)
    for elt in ans:
        print(elt)
    return ans
                







#
if __name__=="__main__":
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    # B = list(map(int, input().split()))
    B = [0 for _ in range(Q)] 
    for i in range(Q):
        B[i] = int(input())
    solve(N,A,Q,B)

