"""
ABC 王国は H 行 W 列のマス目であらわされます。各マスは山のマスと平野のマスのどちらかです。上から i 行目、左から j 列目にあるマスが山のマスなら c 
i,j
​
  は # 、平野のマスなら c 
i,j
​
  は . です。

あなたは鉄道路線を作りたいです。鉄道路線の経路は、以下の条件をすべて満たす必要があります。

条件1　あるマスを始点とし、辺を共有して隣接するマスに移動することを k 回 (3≤k) 繰り返し、始点で終わる経路である。
条件2　k 回の移動について、移動先は相異なる。（始点と終点は一致してよい）
条件3　山のマスを通らない。

例えば左から 1 番目の鉄道路線は条件を満たしますが、左から 2,3,4,5 番目の鉄道路線は条件を満たしません。

 

鉄道路線が通るマスの数としてあり得る最大値を求めてください。ただし、条件を満たす鉄道路線がない場合は、代わりにそれを報告してください。

how to solve:
スタート地点を全探索
各地点からの探索方法は、再帰関数


https://github.com/E869120/kyopro_educational_90/blob/main/sol/072.cpp

俺の疑問：DFSの各ブランチにそれぞれ異なる状態のGridを渡さなきゃいけないから、いちいちgridをこぴーする必要がある？？
解答：　注意深く考えると、DFSって各ブランチが同時実行されているわけではなくて、一番最初のやつから、実行されている。だから、

def dfs
	used[px][py] = true;  <-- 

    dfs/dfs/dfs/.../dfs

	used[px][py] = false;  <-- ここで元にもどせばいいというカラクリがある

"""

def solve(H, W, grid):
    used = [[False for _ in range(W)] for _ in range(H)]
    cur_max = -1
    for i in range(H):
        for j in range(W):
            cur_max = max(search(i, j, i, j, grid, H, W, used, 0), cur_max)
    if cur_max >= 3:
        print(cur_max) 
    else:
        print(-1)
    return 


def search(sx, sy, i, j, grid, H, W, used, cur_len):
    # 終了条件

    # ちゃんと辿り着いた
    if i == sx and j == sy and used[i][j]==True:
        return cur_len

    # 進めない場所に来てしまった
    
    if i<0 or i>=H or j<0 or j>=W or used[i][j]==True:
        return -1  #

    # 再帰
    used[i][j] = True

    cur_max = -1
    cur_max = max(search(sx, sy, i+1, j, grid, H, W, used, cur_len+1), cur_max)
    cur_max = max(search(sx, sy, i, j+1, grid, H, W, used, cur_len+1), cur_max)
    cur_max = max(search(sx, sy, i-1, j, grid, H, W, used, cur_len+1), cur_max)
    cur_max = max(search(sx, sy, i, j-1, grid, H, W, used, cur_len+1), cur_max)

    used[i][j] = False

    return cur_max

def input_args():
    H, W = map(int, input().split())
    C = []
    for _ in range(H):
        c = list(input())
        C.append(c)
    return [H, W, C]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)