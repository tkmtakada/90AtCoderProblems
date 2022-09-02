

def solve(N, S):

    # run length
    cnt = 0
    rl = []
    for i in range(len(S)):
        cnt += 1
        if i == len(S)-1 or S[i] != S[i+1]:
            rl.append((S[i], cnt))
            cnt = 0

    return 



def input_args():
    N = int(input())
    S = list(input())
    return [N, S]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)