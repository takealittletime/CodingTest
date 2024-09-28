import sys
input = sys.stdin.readline

# 테스트 케이스 입력
T = int(input())
# 테스트 케이스만큼 반복
for _ in range(T):
    # 지원자 수 입력
    N = int(input())
    # 지원자 서류, 면접 순위 리스트에 입력
    volunterrs = []
    for _ in range(N):
        doc, interview = map(int,input().split())
        volunterrs.append((doc,interview))
    
    # 서류 심사 결과를 기준으로 오름차순 정렬.
    volunterrs.sort(key = lambda x:x[0])

    # 결과 (신입사원 최대 인원 수)
    count = 1
    # 서류 제일 잘 본 지원자의 면접 순위
    best_interview = volunterrs[0][1]

    for i in range(1,N):
        if volunterrs[i][1] < best_interview:
            best_interview = volunterrs[i][1]
            count += 1
    print(count)