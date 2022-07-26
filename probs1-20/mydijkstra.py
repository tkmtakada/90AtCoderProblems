import heapq

def dijkstra(edges, num_node, street):
    # min_cost = [(float('inf'), i) for i in range(num_node)]
    # min_cost[0][0] = 0
    """
    Qとdistanceは分けた方がいい、Qの中身はpopで消えてしまうので
    """
    dist = [float('inf') for _ in range(num_node)] 
    dist[0] = 0
    Q = []  # (cost, pos)を格納していく
    heapq.heapify(Q)
    heapq.heappush(Q, (0, street))

    # heapq.heapify(min_cost)
    
    while len(Q) > 0:
        cost, cur_pos = Q[0]
        heapq.heappop(Q)

        for pos, cost in edges[cur_pos]:
            if dist[cur_pos] + cost < dist[pos]:
                dist[pos] = dist[cur_pos] + cost
                heapq.heappush(Q, (dist[pos], pos))                
    return dist


if __name__ == '__main__':
    Edges = [
        [[1, 4], [2, 3]],             # ← node 0からの辺のリスト
        [[2, 1], [3, 1], [4, 5]],   # ← node1からの辺のリスト
        [[5, 2]],                       # ← 頂点Cからの辺のリスト
        [[4, 3]],                       # ← 頂点Dからの辺のリスト
        [[6, 2]],                       # ← 頂点Eからの辺のリスト
        [[4, 1], [6, 4]],             # ← 頂点Fからの辺のリスト
        []                                # ← node 6からの辺のリスト
        ]

    #今の目的地の数は7つ（0~6: A~G）
    node_num = 7

    print(dijkstra(Edges, node_num, 0))

