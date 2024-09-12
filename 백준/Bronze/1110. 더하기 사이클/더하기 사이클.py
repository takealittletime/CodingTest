#1110 더하기 사이클

#입/출력 stdin, stdout 사용
import sys
input = sys.stdin.readline

#더하기 사이클 함수
def plusCycle(N):
    if N == 0:
        return 1
    
    length = 0 #리턴할 사이클의 길이

    tmp = 0 #중간에 만들어지는 새로운 수를 할당받을 변수

    #중간에 만들어지는 수와 N이 같아질 떄까지 반복
    while (tmp != N):
        #첫 반복 시 N을 가지고 새로운 값 생성
        if length == 0:
            #a에는 일의 자리 수 계산, b에는 십의 자리 수 계산 후 합침.
            a = (N // 10 + N % 10) % 10
            b = (N % 10) * 10
            tmp =  a + b
            length += 1
        #이후부터는 tmp값을 가지고 새로운 값 생성
        else:
            #a에는 일의 자리 수 계산, b에는 십의 자리 수 계산 후 합침.
            a = (tmp // 10 + tmp % 10) % 10
            b = (tmp % 10) * 10
            tmp =  a + b
            length += 1
    #총 사이클의 길이 리턴
    return length

#첫째 줄에 N 입력
N = int(input().rstrip())

#첫째 줄에 N의 사이클 길이 출력
sys.stdout.write(str(plusCycle(N))+'\n')