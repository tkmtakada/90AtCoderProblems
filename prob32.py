

def solve(N, A, M, NG):
    canRunList = [True for _ in range(N)]  # True for available member

    time = 0
    dfs(N, A, M, NG, runnerIdx, canRunList, time)

def dfs(N, A, M, NG, runnerIdx, canRunList, time):
    # 終了条件
    next_cands = []
    for idx, canRun in enumerate(canRunList):
        if canRun:
            next_cands.appned(idx) 
    if not next_cands:
        return -1




def input_args():
    N = int(input())
    A = []
    for _ in range(N):
        a = list(map(int, input().split()))
        A.append(a)
    M = int(input())
    NG = []
    for _ in range(M):
        ng = list(map(int, input().split()))
        NG.append(ng) 
    return [N, A, M, NG]

def test():
   return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)