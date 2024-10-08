import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answer = input().rstrip()
    record = 0
    tmp = 0
    for ans in answer:
        if ans == 'O':
            tmp += 1
            record += tmp
        if ans == 'X':
            tmp = 0
    print(record)