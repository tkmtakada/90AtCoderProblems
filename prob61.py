from collections import deque

def solve(Q, query):
    queue = deque([])  # 左が下、右が上
    for t, x in query:
        if t == 1:
            queue.append(x)
        elif t == 2:
            queue.appendleft(x)
        elif t == 3:
            print(queue[-x])
    return 0



def input_args():
    Q = int(input())
    query = []
    for _ in range(Q):
        q = list(map(int, input().split()))
        query.append(q)
    return [Q, query]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)