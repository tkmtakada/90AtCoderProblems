

def solve(N, S):
    """
    idsList[i][j]: S[:j+1]までの文字列で、
    atcoderという文字のi番目までの文字の作り方を格納
    // 上と左にdummy列が挿入されている
    """
    S = "#" + S
    N = N+1

    atcoder = "atcoder"
    arr = [[0 for _ in range(N)] for _ in atcoder]    
    # 最初のaを見つける
    for i in range(len(S)):
        if S[i] == 'a':
            firstIidx = i
            break
    arr[0][firstIidx] = 1
    
    for j in range(firstIidx+1, N):
        for i in range(len(atcoder)):
            arr[i][j] += arr[i][j-1]
            # もしも、今ひいた文字が戦況を変えうる文字だったら
            if S[j] == atcoder[i]: arr[i][j] += arr[i-1][j-1]
    ans = arr[-1][-1]
    print(ans)



def input_args():
    N = int(input())
    S = input()
    return [N, S]

def test():
    N = 10
    S = "attcordeer"
    return [N, S]

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)