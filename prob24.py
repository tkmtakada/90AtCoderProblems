

def solve(N, K, A, B):
    counter = 0
    for a, b in zip(A, B):
        counter += abs(a-b)

    if counter > K:
        print("No")
    else:
        if (K - counter) % 2 == 0:
            print("Yes")
        else:
            print("No")
    return 0


def input_args():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    return [N, K ,A, B]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)