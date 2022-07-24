

def solve(N, C, P, Q, L, R, cumP):
    for l, r in zip(L,R):
        total1 = cumP[0][r] - cumP[0][l-1]
        total2 = cumP[1][r] - cumP[1][l-1]
        print(total1, total2)



def input_args():
    N = int(input())
    C = [0 for _ in range(N)]
    P = [0 for _ in range(N)]
    cumP = [[0 for _ in range(N+1)] for _ in range(2)]  # 先頭にdummyの0をつけておくと便利
    for i in range(N):
        C[i], P[i] = map(int, input().split())
        # cumsumを計算しておく
        if C[i] == 1:
            cumP[0][i+1] = cumP[0][i] + P[i]
            cumP[1][i+1] = cumP[1][i]
        elif C[i] == 2:
            cumP[0][i+1] = cumP[0][i]
            cumP[1][i+1] = cumP[1][i] + P[i]


    Q = int(input())
    L = [0 for _ in range(Q)]
    R = [0 for _ in range(Q)]
    for i in range(Q):
        L[i], R[i] = map(int, input().split())
    
    return [N, C, P, Q, L, R, cumP]

def test():
   return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)