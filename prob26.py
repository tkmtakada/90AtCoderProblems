
"""
edges: 入っているnodeの名前は0スタートになっている
"""
def solve(N, edges):
    # create adj table
    adj = [[] for _ in range(N)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    avail = [True] * N
    # 最後インデックスをなおすの忘れずに！
    ans = []
    ret = dfs(adj, avail, N, ans)
    print([elt + 1 for elt in ret])
    return 0

def dfs(adj, avail, N, ans):

    # 終了判定 and 次の一個を決める
    if len(ans) == N / 2:
        return ans

    next_cands = []
    for i in range(N):
        if avail[i] == True:
            next_cands.append(i)
    if not next_cands:  # len(ans) != N/2のため、このpathは不正解
            return  
    
    for cand in next_cands:
        updatedAvail = avail
        updatedAvail[cand] = False        
        # neightborもfalseにする
        for neighbor in adj[cand]:
            updatedAvail[neighbor] = False
        ret = dfs(adj, updatedAvail, N, ans+[cand])
        if ret is not None:
            return ret

def input_args():
    N = int(input())
    edges = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        edges.append([a-1, b-1])
    return [N, edges]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)