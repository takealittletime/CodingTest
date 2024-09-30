# 입력에 stdin 이용
import sys
input = sys.stdin.readline

# 두 문자열 입력
str1 = list(input().rstrip())
str2 = list(input().rstrip())
# lcs 2차원 배열 0으로 초기화
lcs = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

# 2차원 배열 순회하면서
for i in range(1, len(str1)+1):
    for j in range(1,len(str2)+1):
        # 두 문자열의 내용이 같다면
        if str1[i-1] == str2[j-1]:
            # lcs[i-1][j-1] 값에서 +1 해서 채워넣기
            lcs[i][j] = lcs[i-1][j-1] + 1
        # 두 문자열의 내용이 다르다면
        else:
            # 위/왼쪽 값 중 큰 값 가져오기
            lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
# 결과 출력
print(max(map(max,lcs)))