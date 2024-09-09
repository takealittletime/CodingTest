import sys
input = sys.stdin.read

def stack_operations(commands):
    stack = []
    result = []
    
    for command in commands:
        if command[0] == "push":
            stack.append(int(command[1]))
        elif command[0] == "pop":
            if stack:
                result.append(stack.pop())
            else:
                result.append(-1)
        elif command[0] == "size":
            result.append(len(stack))
        elif command[0] == "empty":
            if stack:
                result.append(0)
            else:
                result.append(1)
        elif command[0] == "top":
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)
    
    return result

# 입력 처리
commands = input().splitlines()
commands = [command.split() for command in commands[1:]]  # 첫 줄은 명령 수이므로 무시

# 결과 처리
output = stack_operations(commands)
print("\n".join(map(str, output)))
