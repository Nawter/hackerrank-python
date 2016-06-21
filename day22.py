class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


    def getHeightInternal(self, root, m):
        if not root:
            return m
        return max(self.getHeightInternal(root.left, m+1), self.getHeightInternal(root.right, m+1))
    
    def getHeight(self, root):
        return self.getHeightInternal(root, 0)-1

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height        