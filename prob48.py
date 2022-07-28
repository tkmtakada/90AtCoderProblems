import heapq

def solve(N, K, A, B):
    # A, Bはマイナスでいれている、heapqを使うために
    heapq.heapify(B)
    
    total = 0
    for i in range(K):
        minv = heapq.heappop(B)
        # print("Val: ", minv)
        total += minv[0]
        if minv[1] == 'B':
            heapq.heappush(B, A[minv[2]])
    print(-total)



def input_args():
    N, K = map(int, input().split())
    A = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = (-(a-b), 'A', i)
        B[i] = (-b, 'B', i)        

    return [N, K, A, B]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)