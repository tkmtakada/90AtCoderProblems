def solve2(N, P, Q, originalA):
    A = [a % P for a in originalA]
    ans = 0
    for i in range(N-4):
        for j in range(i+1, N-3):
            for k in range(j+1, N-2):
                for l in range(k+1, N-1):
                    for m in range(l+1, N):
                        # prod = A[i] * A[j] * A[k] * A[l] * A[m]
                        # if prod in [Q, Q+P, Q+(2*P), Q+(3*P), Q+(4*P)]:
                        prod = 1
                        for idx in [i,j,k,l,m]:
                            prod *= A[idx]
                            prod %= P
                        if prod == Q:
                            ans += 1
                            # print(originalA[i],
                            #         originalA[j],
                            #         originalA[k],
                            #         originalA[l],
                            #         originalA[m])
    print(ans)



def solve(N, P, Q, A):
    mp = {}
    for elt in A:
        a = elt % P
        if a in mp:
            mp[a] += 1
        else:
            mp[a] = 1
    
    
    ...

def dfs(path, curDepth, cands, ans):

    # 終了条件
    # 
    # もしもすでに長さが5なら終わりで判定
    # 長さはまだ5未満だけど、次のcanddaiteがなくても終わり
    ...


def input_args():
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    return [N, P, Q, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve2(*args)