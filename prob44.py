from collections import deque

def solve(N, Q, A, Qs):    
    for q in Qs:
        if q[0] == 1:
            x, y = q[1]-1, q[2]-1
            A[x], A[y] = A[y], A[x]
        elif q[0] == 2:
            a = A.pop()
            A.appendleft(a)
        elif q[0] == 3:
            print(A[q[1]-1])


def input_args():
    N, Q = map(int, input().split())
    A = deque(list(map(int, input().split())))
    Qs = []
    for i in range(Q):
        Qs.append(list(map(int, input().split())))
    return [N, Q, A, Qs]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)