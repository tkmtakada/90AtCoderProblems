
mod = 10 ** 9 + 7
def solve(N, A):
    ans = 1
    for lst in A:
        ans *= sum(lst)
        ans %= mod
    print(ans)



def input_args():
    N = int(input())
    A = []
    for _ in range(N):
        a = list(map(int, input().split()))
        A.append(a)
    return [N, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)