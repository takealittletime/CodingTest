# 입력에 stdin 사용
import sys
input = sys.stdin.readline

# N=멀티탭 구멍 개수, K=전기용품 사용횟수
N, K = map(int,input().split())
# 전기용품 입력 받음
electronics= list(map(int,input().split()))
# plugs는 사이즈K의 배열로 생각.
plugs = []

# 결과 할당할 변수 count
count = 0

# 전기용품 사용횟수만큼 반복
for i in range(K):
    # 이미 꽂혀있는 전자기기일 때 continue
    if electronics[i] in plugs:
        continue
    
    # 플러그에 구멍 남아있을 때
    if len(plugs) < N:
        # 전기용품 꽂고 continue
        plugs.append(electronics[i])
        continue
    
    # 꽂혀있는 플러그에서 우선순위를 정할 사이즈 K의 배열로 생각.
    priority = []

    # 이미 플러그에 꽂혀있는 전기용품들에 대해
    for already in plugs:
        # 아직 사용 전인 전기용품들
        rest = electronics[i:]
        # 사용 예정인 제품에 대해 슬라이싱 이후 인덱스 번호를 우선순위로 부여
        if already in rest:
            priority.append(rest.index(already))
        # 사용 예정이 없으면 우선순위를 큰 값(101)으로 채움.
        else:
            priority.append(101)
    
    # 뽑을 플러그의 인덱스를 계산해 target에 할당
    target = priority.index(max(priority))
    # 해당 플러그 제거
    plugs.remove(plugs[target])
    # 결과값 카운트
    count += 1
    # 플러그에 현재 전자기기 꽂기
    plugs.append(electronics[i])
# 결과 출력
print(count)