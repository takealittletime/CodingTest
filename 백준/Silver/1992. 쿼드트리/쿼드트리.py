#1992 쿼드트리

# 입, 출력 stdin, stdout 사용
import sys
input = sys.stdin.read

#분할 정복으로 문제 풀이 (결괏값 반환 부분 미완)
def divide_and_conquer(x, y, n):
    # 결과 리스트 전역변수로 선언
    global result
    # 좌표 상 가장 왼쪽 위 값 가져옴
    num = monitor[x][y]
    # print(num)
    
    # 현재 영역이 모두 같은 색인지 확인
    same_num = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if monitor[i][j] != num:
                same_num = False
                break
        if not same_num:
            break
    
    # 같은 색이면 해당 점을 리스트에 추가
    if same_num:
        if num == '0':
            result.append("0")
        else:
            result.append("1")
    else:
        # 값이 다르면 4개의 영역으로 나누어 재귀적으로 처리
        half = n // 2
        result.append('(')
        divide_and_conquer(x, y, half)        
        divide_and_conquer(x, y + half, half)       
        divide_and_conquer(x + half, y, half)       
        divide_and_conquer(x + half, y + half, half)
        result.append(')')

# 값 입력
data = input().split()

# 첫 번째 줄 N
N = int(data[0])
# 각 문자열 monitor에 2차원 배열 형태로 저장
monitor = [list(x) for x in data[1:]]
result = []

divide_and_conquer(0,0,N)

for r in result:
    print(r,end="")