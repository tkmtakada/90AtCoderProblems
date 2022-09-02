

def solve(N, M, graph):
    return 



def input_args():
    N, M = map(int, input().split())
    graph = []
    for _ in range(M):
        graph.append(list(map(int, input().split())))
    return [N, M, graph]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)