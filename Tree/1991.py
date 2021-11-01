import sys

input = sys.stdin.readline

N = int(input())

tree = {}

for n in range(N):
    root, left, right  = map(input().stript().split())
    tree[root] = [left, right]


# 부모, 좌, 우 
def preOrder(node):
    if node == '.':
        return
    
    print (node, end="")
    preOrder(tree[node][0])
    preOrder(tree[node][1])

# 좌 부모 우 
def inOrder(node):
    if node == '.':
        return

    inOrder(tree[node][0])
    print (node, end="")
    inOrder(tree[node][1])

# 좌 우 부모
def postOrder(node):
    if node == '.':
        return

    postOrder(tree[node][0])
    postOrder(tree[node][1])
    print (node, end="")