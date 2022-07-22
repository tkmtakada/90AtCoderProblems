

def solve(N, M , roads):
    



def input_args():
    N, M = map(int, input().split())
    roads = []
    for i in range(M):
        roads.append(list(map(int, input().split())))
    return [N, M, roads]

def test():
   return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)