"""
uplift
"""

def solve(n, q, A, changes):
    for change in changes:
        l, r, v = change
        for i in range(l-1, r):
            A[i] += v
    
    # take a diff
    val = 0
    for j in range(len(A)-1):
        val += abs(A[j] - A[j+1])

    print(val)
    return val




def input_args():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    changes = []
    for _ in range(q):
        change = list(map(int, input().split()))
        changes.append(change)
    return [n, q, A, changes]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)