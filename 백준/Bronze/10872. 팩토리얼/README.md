# [Bronze III] 팩토리얼 - 10872 

[문제 링크](https://www.acmicpc.net/problem/10872) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

구현, 수학

### 제출 일자

2024년 9월 7일 09:17:45

### 문제 설명

<p>0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.</p>

### 출력 

 <p>첫째 줄에 N!을 출력한다.</p>

> 반복(iteration)으로 푸는 방법
```
N = int(input())

ans = 1

for i in range(2,N+1):
    ans *= i

print(ans)
```

> 재귀함수(recursive)로 푸는 방법

```
def factorial (n):
    if n == 0:
        return 1
    
    else:
        return n*factorial(n-1)
    
N = int(input())

print(factorial(N))
```
