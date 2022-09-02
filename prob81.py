

def solve(N, K, students):
    return 



def input_args():
    N, K = map(int, input().split())
    students = []
    for _ in range(N):
        a, b = map(int, input().split())
        students.append([a, b])
    return [N, K, students]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)