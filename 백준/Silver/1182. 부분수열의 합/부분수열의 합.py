def find_sequence(idx, current_sum):
    global count

    if idx == N:
        if current_sum == S:
            count += 1
        return
    
    find_sequence(idx + 1, current_sum)
    find_sequence(idx + 1, current_sum + nums[idx])


N, S = map(int,input().split())
nums = list(map(int,input().split()))
count = 0
find_sequence(0,0)

# S가 0일 경우, 공집합을 제외해야 함
if S == 0:
    count -= 1

print(count)