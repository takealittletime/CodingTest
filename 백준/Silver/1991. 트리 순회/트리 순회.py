class BinaryTree:
    def __init__(self):
        self.tree = {}

    def add_node(self,root,left,right):
        self.tree[root] = [left, right]
    
    def pre_order(self,node):
        if node == '.':
            return
        print(node,end='')
        self.pre_order(self.tree[node][0])
        self.pre_order(self.tree[node][1])
    
    def in_order(self,node):
        if node == '.':
            return
        self.in_order(self.tree[node][0])
        print(node,end='')
        self.in_order(self.tree[node][1])
    
    def post_order(self,node):
        if node == '.':
            return
        self.post_order(self.tree[node][0])
        self.post_order(self.tree[node][1])
        print(node,end='')
    
N = int(input())
binaryTree = BinaryTree()
for i in range(N):
    root, left, right = input().split()
    binaryTree.add_node(root,left,right)

binaryTree.pre_order('A')
print()
binaryTree.in_order('A')
print()
binaryTree.post_order('A')
print()