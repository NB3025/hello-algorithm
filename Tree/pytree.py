#하나의 뿌리에서 위로 뻗어나가는 형상
# 트리는 자식도 트리고 또 그자식도 트리
# RootNode
# / 간선 (edge)
# 내부노드(internal node)
# 단말노드 (terminal node)

#트리는 항상 루트에서 시작된다
#루트는 자식 노드를 가지며, 간선으로 연결되어 있다
# 자식 노드의 개수는 차수라고 한다
# 크기는 자신을 포함한 모든 자식 노드의 갯수
# 높이는 현재 위치에서 리프까지의 거리, 깊이는 루트에서부터 현재 노드까지의 거리

#트리는 순환구조를 갖지 않는 그래프
# 핵심은 순환구조가 아니다.

#Binary Tree
#자식노드를 두 개 이하만 갖는 트리

#완전 이진트리
# 왼쪽부터 모든 자식노드가 채워져있음. 마지막 우측노드는 안채워져있을수 있음

#포화 이진트리 

#Non-Binary tree
# 대표적인 사용처가 trie 컴퓨터 검색을 뜻하는 retrieval에서 온 단어
# 시간복잡도가 O(m)이므로 문자열 검색에 특화된 자료구조

# 트리 노드 클래스
# 멤버 3개

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print (self.data)
        if self.right:
            self.right.PrintTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()