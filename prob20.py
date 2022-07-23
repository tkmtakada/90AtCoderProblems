

def solve(a, b, c):
    # a < b^c ? 
    ...
    if a < c ** b:
        print("Yes")
    else:
        print("No")
    return 0


def input_args():
    a, b, c = map(int, input().split())
    return [a, b, c]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)