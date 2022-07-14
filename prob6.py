alphabets = "abcdefghijklmnopqrstuvwxyz"
len_alphabets = len(alphabets)
nums = [i for i in range(len_alphabets)]
mp = {}
num2alph = {} 
for s, num in zip(alphabets, nums):
    mp[s] = num
    num2alph[num] = s


"""
solve2じゃないとTLE
"""
def solve(N, K, seq):
    ans = []
    for k in reversed(range(K)):
        # startは後ろからk番目
        curMin = 'zz'
        curMinIdx = 0
        for i in reversed(range(N-k)):
            # for s in reversed(seq[:N-k]):
            s = seq[i]
            if s <= curMin: 
                curMin = s 
                curMinIdx = i

        # seqを更新、答えをリストに格納
        ans.append(curMin)        
        seq = seq[curMinIdx+1:]
        N = len(seq)
    ret = "".join(ans)
    print(ret)
    return ret

"""
やっていることはムズカしく見えるが、ただのoperation.実験をすればすぐわかる
"""
def solve2(N, K, seq):
    table = [['#' for _ in range(N+1)] for _ in range(len_alphabets)]
    
    for i in reversed(range(len(seq))):  # len(seq) = Nだとは思うが
        s = seq[i]
        num = mp[s]
        # 先に、一個先の情報を全部コピーする
        for j in range(len_alphabets):
            table[j][i] = table[j][i+1]
        table[num][i] = i
    # ここまでで、tableの用意完了
    # ここから、最小のsubsequenceを作っていく
    ans = []
    
    curIdx = 0
    restLength = K
    while len(ans) < K:
        for j in range(len_alphabets):
            if table[j][curIdx] != '#' and  table[j][curIdx] <= N-restLength:
                ans.append(num2alph[j])
                break
        curIdx = table[j][curIdx] + 1
        restLength -= 1
    ret = "".join(ans)
    print(ret)
    return ret




#
if __name__=="__main__":
    N, K = map(int, input().split())
    seq = input()
    # N, K = 89, 3
    # seq = "rmxbtwjuxnnnrilidhtzuoibdhjajywjmdembpgtgpfkesyycuxybslioryvcetxnodhgxxahsyairkdnbiyuaazd"
    solve2(N,K,seq)
