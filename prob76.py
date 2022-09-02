
"""
sliding window??
"""
from collections import deque

def solve(N, A):
    total = sum(A)
    thr = total // 10
    if thr * 10 != total:  # 割り切れた
        print("No")
        return 

    cur = 0
    q = deque()
    A2= A + A
    for elt in A2:
        cur += elt
        q.append(elt)
        
         # judge
        if cur == thr:
            print('Yes')
            return 

        while cur > thr:
            r = q.popleft()
            cur -= r  # 必ずどこかのタイミングで0になり、そのときにWhileは必ず抜けられる

         # judge
        if cur == thr:
            print('Yes')
            return 
    print('No')
    return 



def input_args():
    N = int(input())
    A = list(map(int, input().split()))
    return [N, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)