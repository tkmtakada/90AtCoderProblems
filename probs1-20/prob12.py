

def solve(H, W, Q, queries):
    grid = [[0 for _ in range(W)] for _ in range(H)]
    for q in queries:
        # print(grid)
        if q[0] == 1:
            r, c = q[1], q[2]
            grid[r-1][c-1] = 1  # インデックス調整
        elif q[0] == 2:
            ra, ca, rb, cb = q[1:]
            print(isReachable(grid, ra-1, ca-1, rb-1, cb-1, H, W))

def isReachable(grid, ra, ca, rb, cb, H, W):
    # 始点、終点もredに塗られている必要あり
    # まずはDFSでやってみるか
    if grid[ra][ca] == 0:
        return "No"

    if bfs(grid, ra, ca, rb, cb, H, W):
        return "Yes"
    else:
        return "No"
    

def dfs(grid,visited, i, j, rb, cb, H, W):
    # 終了条件
    if i<0 or i>=H or j<0 or j>=W or grid[i][j] != 1 or visited[i][j]==True:  # 一つでも成り立ってしまったらアウト
        return False
    
    if (i, j) == (rb, cb):
        return True
    
    # 処理
    visited[i][j]=True

    # 枝分かれ実行
    ret1 = dfs(grid, visited, i+1, j, rb, cb, H, W)
    if ret1: return True
    
    ret2 = dfs(grid, visited, i, j+1, rb, cb, H, W)
    if ret2: return True

    ret3 = dfs(grid, visited, i-1, j, rb, cb, H, W)
    if ret2: return True

    ret4 = dfs(grid, visited, i, j-1, rb, cb, H, W)
    if ret4: return True

def bfs(grid, i, j, rb, cb, H, W):
    queue = [(i, j)]
    visited = set([(i, j)])
    while len(queue) > 0:
        len_queue = len(queue)
        # print(queue)
        for i in range(len_queue):
            cur = queue.pop()
            if cur == (rb, cb):
                return True
            # visited.add(cur)
            # queueに次の候補をappend
            nextPath = getNextPath(grid, cur[0], cur[1], H, W, visited)
            queue.extend(nextPath)
            visited = visited.union(set(nextPath))  # ここで訪れたことあるの追加
    
    # while文を抜けてしまったら、targetにたどりつけなかったということ
    return False

def getNextPath(grid, i, j, H, W, visited):
    nextPath = []
    for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
        # print("r, c: ", r, c)
        if 0<=r and r<H and 0<=c and c<W and grid[r][c]==1 and (r, c) not in visited:
            nextPath.append((r, c))
    return nextPath




def input_args():
    H, W = map(int, input().split())
    Q = int(input())
    queries = []
    for _ in range(Q):
        q = list(map(int, input().split()))
        queries.append(q)
    return [H, W, Q, queries]

def test():
    H, W = 2, 2
    Q = 4
    queries = [[1, 2, 2],
            [1, 1, 2],
            [1, 1, 1],
            [2, 1, 1, 2, 2]]
    return [H, W, Q, queries]

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)