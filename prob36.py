import math

def solve(A, B):
    mod = 10e18
    gcd = math.gcd(A, B)
    r = B / gcd
    if r > (10e18 / A):
        print("Large")
    else:
        print(r * A)
    return 
    a = A // gcd 
    b = B // gcd
    # 大きさチェック
    # if math.log10(a) + math.log10(b) + math.log10(gcd) > 18:
    r = a * b * gcd
    if r > 10e18:
        print("large")
    else:
        print(r)



def input_args():
    A, B = map(int, input().split())    
    return [A, B]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)