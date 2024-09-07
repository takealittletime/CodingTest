# [Gold V] 하노이 탑 - 1914 

[문제 링크](https://www.acmicpc.net/problem/1914) 

### 성능 요약

메모리: 31120 KB, 시간: 724 ms

### 분류

임의 정밀도 / 큰 수 연산, 재귀

### 제출 일자

2024년 9월 7일 10:45:33

### 문제 설명

<p>세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.</p>

<ol>
	<li>한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.</li>
	<li>쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.</li>
</ol>

<p>이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.</p>

<p>아래 그림은 원판이 5개인 경우의 예시이다.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11729/hanoi.png" style="height:200px; width:1050px"></p>

### 입력 

 <p>첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 100)이 주어진다.</p>

### 출력 

 <p>첫째 줄에 옮긴 횟수 K를 출력한다.</p>

<p>N이 20 이하인 입력에 대해서는 두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다. N이 20보다 큰 경우에는 과정은 출력할 필요가 없다.</p>

>재귀적 방법 recursive
```
def hanoi(n, start, end, mid):
    # 원판이 1개일 때 바로 옮김
    if n == 1:
        print(start, end)
        return
    # n-1개의 원판을 start -> mid로 옮김 (재귀 호출)
    hanoi(n - 1, start, mid, end)
    # 가장 큰 원판을 start -> end로 옮김
    print(start, end)
    # n-1개의 원판을 mid -> end로 옮김 (재귀 호출)
    hanoi(n - 1, mid, end, start)

# 입력 처리
N = int(input())

# 총 이동 횟수는 2^N - 1 (하노이의 탑 공식)
total_moves = 2**N - 1
print(total_moves)

# N이 20 이하일 때만 과정을 출력
if N <= 20:
    hanoi(N, 1, 3, 2)  # 1번 장대에서 3번 장대로, 2번 장대를 보조로 사용

```

>반복적 방법 iteration
```
def hanoi_iterative(n):
    # 이동 횟수는 2^N - 1
    total_moves = 2**n - 1
    print(total_moves)
    
    # 장대의 초기 설정
    from collections import deque
    
    # 스택을 사용하여 상태를 저장
    stack = deque()
    
    # 초기 상태를 스택에 추가 (n, start, end, mid)
    stack.append((n, 1, 3, 2))
    
    # 반복문을 통해 상태를 처리
    while stack:
        num, start, end, mid = stack.pop()
        
        if num == 1:
            print(start, end)
        else:
            # 문제를 세 부분으로 나눠서 스택에 추가
            stack.append((num - 1, mid, end, start))  # n-1개를 중간 장대에서 목표 장대로
            stack.append((1, start, end, mid))        # 가장 큰 원판을 시작 장대에서 목표 장대로
            stack.append((num - 1, start, mid, end))  # n-1개를 시작 장대에서 중간 장대로

# 입력 처리
N = int(input().strip())
hanoi_iterative(N)
```
