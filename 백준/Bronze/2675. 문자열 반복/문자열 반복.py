T = int(input().strip())

for i in range(T):
    R, S = input().split()
    R = int(R)
    P = ""

    for character in S:
        for j in range(R):
            P += character
    print(P)  # 이 부분이 바깥쪽 for 루프에 맞춰 들여쓰기 되어야 합니다.
