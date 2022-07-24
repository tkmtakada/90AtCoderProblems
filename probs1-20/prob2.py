def dfs(seq, L, R, ans, K):
    # 終了条件
    if len(L) == 0 and len(R) == 0:
        ans.append("".join(seq))

    # numL, numRはL, Rのながさから逆算できる
    numL = K - len(L)
    numR = K - len(R)

    if len(L) >= 1:  #   if L is Appendable
        dfs(seq + ['('], L[1:], R, ans, K)
    if numR < numL:  # if R is appendable
        dfs(seq + [')'], L, R[1:], ans, K)


def solve(N):
    K = int(N / 2)
    
    seq = ['(']    
    L = ['('] * (K - 1)
    R = [')'] * K
    ans = []
    numL = 1
    numR = 0
    dfs(seq, L, R, ans, K)

    # output
    for seq in ans:
        print(seq)



#
if __name__=="__main__":
    N = int(input())
    # N = 10
    if N%2 == 0:
        solve(N)
    else:
        pass 
