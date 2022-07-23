import math

def solve(T, L, X, Y, Q, time):
    w = 2 * math.pi / T
    for t in time:
        y = -(L / 2) * math.sin(w * t)
        d = math.sqrt((Y-y)**2 + X**2)
        height = (L/2) * (1- math.cos(w*t))
        theta = math.atan(height/d)
        print(theta * (180 / math.pi))



def input_args():
    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())
    time = []
    for _ in range(Q):
        time.append(int(input()))
    return [T, L, X, Y, Q, time]

def test():
   return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)