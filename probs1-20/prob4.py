
def solve(arr):
    H = len(arr)
    W = len(arr[0])
    sumAxis0 = [sum(vec) for vec in arr]  # 長さ H
    sumAxis1 = [0 for _ in range(W)]  # 長さW
    for i in range(W):
        for j in range(H):
            sumAxis1[i] += arr[j][i]

    ans = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            ans[i][j] = sumAxis0[i] + sumAxis1[j] - arr[i][j]
        print(*ans[i])
    
    # print






#
if __name__=="__main__":
    H, W = map(int, input().split())
    arr = [0 for i in range(H)]
    for i in range(H):
        arr[i] = list(map(int, input().split()))
    solve(arr)
