def get_tree_length(trees, height):
    # 나무들을 height에서 잘랐을 때 가져갈 수 있는 총 나무 길이 계산
    total = 0
    for tree in trees:
        if tree > height:
            total += tree - height
    return total

def find_max_height(trees, M):
    low, high = 0, max(trees)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        # 중간값(mid)에서 나무를 자르고 나무 길이 계산
        obtained_wood = get_tree_length(trees, mid)
        
        if obtained_wood >= M:
            # 나무를 충분히 가져갈 수 있으면, 높이를 더 올려본다
            result = mid
            low = mid + 1
        else:
            # 나무가 부족하면 절단기의 높이를 낮춘다
            high = mid - 1
    
    return result

# 입력 받기
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 절단기 높이의 최댓값 찾기
max_height = find_max_height(trees, M)
print(max_height)
