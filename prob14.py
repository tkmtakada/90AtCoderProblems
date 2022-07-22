

def solve(N, A, B):
    A.sort()
    B.sort()
    total = 0
    for i in range(N):
        total += abs(A[i] - B[i])
    print(total)


def input_args():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    return [N, A, B]

def test():
   return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)