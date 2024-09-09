def divide_conquer(x,y,n):
    global white, blue

    color = paper[x][y]
    same_color = True

    for i in range(x, x+n):
        for j in range(y, y+n):
            if (paper[i][j] != color):
                same_color = False
                break
        if not same_color:
            break
    
    half = n//2

    if same_color:
        if color == 0:
            white += 1
        else:
            blue += 1
    
    else:
        divide_conquer(x,y,half) #1사분면
        divide_conquer(x,y+half,half) #2사분면
        divide_conquer(x+half,y,half) #3사분면
        divide_conquer(x+half,y+half,half) #4사분면


N = int(input())

paper = [ list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

divide_conquer(0,0,N)

print(white)
print(blue)