

def solve(H, W, x0, y0, x1, y1, grid):
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] == ".":
                

    return 0



def input_args():
    return []

def test():
    H, W = 3, 3
    x0, y0 = 1, 1
    x1, y1 = 3, 3
    grid = [list("..#"),
            list("#.#"),
            list("#..")]

    return [H, W, x0, y0, x1, y1, grid]

if __name__=="__main__":
    # args = input_args()
    args = test()
    solve(*args)