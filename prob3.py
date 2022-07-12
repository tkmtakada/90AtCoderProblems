
"""
アルゴリズムは正しい。けど、C++じゃないせいで最終問題でTLE
起こしている.あれ、と思ったら、PyPyじゃなくて、Pythonにしたら通った

"""

def bfs(adj, curPos):    
    queue = [curPos]
    dist = ['#'] * len(adj)
    dist[curPos] = 0
    depth = 0
    while len(queue) > 0:
        # print(depth, queue)
        for _ in range(len(queue)):
            node = queue.pop(0)

            # このnodeまでの距離をメモ
            for nextNode in adj[node]:
                if dist[nextNode] == '#':  # 未探索の意味
                    dist[nextNode] = dist[node] + 1
                    queue.append(nextNode)            
        depth += 1
    # print("depth, curPos",depth, curPos)
    return depth, nextNode





def solve(adj):
    # 全のーど探す
    # edgeNode = []
    # for i in range(len(adj)):
    #     if len(adj[i]) == 1:
    #         edgeNode.append(i)
    # # 循環はない、都市数Nにたいして道 N-1だから

    # curMax = -1
    # for node in edgeNode:
    #     depth = bfs(adj, node)
    #     curMax = max(curMax, depth)
    """
    木の直径は、最長距離を２回だせばいいらしい
    """
    depth, end = bfs(adj, 0)
    depth, end = bfs(adj, end)
    
    print(depth+1)
    
#
if __name__=="__main__":
    N = int(input())
    adj = [[] for i in range(N)]
    for i in range(N-1):  # 入力は道の数だけしかこない
        A, B = map(int, input().split())
        adj[A-1].append(B-1)
        adj[B-1].append(A-1)
    # adj = [[1], [0,2], [1]]
    # adj = [[1], [0, 2], [1, 3, 4], [2], [2]]
    # print("adj",adj)
    solve(adj)
    
