import sys

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 반복적인 삽입 메소드
    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key < current.value:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    # 반복적인 후위 순회
    def postorder_iterative(self, node):
        if node is None:
            return
        
        stack, output = [], []
        current = node
        
        while stack or current:
            if current:
                stack.append(current)
                output.append(current.value)
                current = current.right  # 먼저 오른쪽 자식으로 이동
            else:
                current = stack.pop()
                current = current.left  # 스택에서 꺼낸 후 왼쪽 자식으로 이동
        
        # 후위 순회이므로 결과를 뒤집는다
        for value in reversed(output):
            print(value)

# 입력 처리 및 트리 생성
bst = BinarySearchTree()
datas = list(map(int, sys.stdin.read().splitlines()))

for data in datas:
    bst.insert(data)

bst.postorder_iterative(bst.root)
