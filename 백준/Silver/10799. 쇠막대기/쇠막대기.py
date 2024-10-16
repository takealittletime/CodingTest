import sys
input = sys.stdin.readline

data = input().rstrip()
stack = []
stick = 0
count = 0

for i in range(len(data)):
    if data[i] == '(':
        stack.append(data[i])
    else:
        if data[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)