
import math

mod = 2**31 -1
def solve(A, B, C):
    minV = min(A, B, C)
    gdv = 1
    for i in reversed(range(1, minV+1)):
        if A % i == 0 and B % i == 0 and C % i == 0:
            gdv = i
            break
    count = A / gdv + B /gdv + C / gdv - 3
    print(int(count))
    return 0

def solve2(A, B, C):
    gcd = int(math.gcd(A, math.gcd(B, C)))
    # print(gcd)
    a = A // gcd 
    b = B // gcd 
    c = C // gcd
    count = a + b + c - 3
    print(int(count))
    return 0

def input_args():
    A, B, C = map(int, input().split())
    return [A, B, C]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve2(*args)