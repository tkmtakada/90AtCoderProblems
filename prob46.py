

def solve(N, A, B, C):
    mp_a, mp_b, mp_c = {}, {}, {}
    for mp, lst in zip([mp_a, mp_b, mp_c], [A, B, C]):
        for num in lst:
            r = num % 46
            if r in mp:
                mp[r] += 1
            else:
                mp[r] = 1    
    # ここまでで準備完了
    ans = 0
    for key_a, val_a in mp_a.items():
        for key_b, val_b in mp_b.items():
            cur_sum = key_a + key_b
            # 46　or 92
            for target_q in [0, 46, 92]:
                val_c = target_q - (key_a + key_b)
                if val_c in mp_c:
                    ans += val_a * val_b * mp_c[val_c]

    print(ans)
    return 0





def input_args():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    return [N, A, B, C]

def test():
    N = 3
    A= [10, 13, 93]
    B= [5, 27, 35]
    C= [55, 28, 52]
    return [N, A, B, C]

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)