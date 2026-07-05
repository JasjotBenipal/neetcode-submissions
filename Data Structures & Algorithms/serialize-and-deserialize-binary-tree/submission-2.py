# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        return ",".join(str(item) for item in result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        result = []
        strin = data.split(",")
        if strin[0] == "None":
            return None
        root = TreeNode(strin[0])
        queue = collections.deque()
        queue.append(root)

        index = 1
        while queue:
            node = queue.popleft()
            if strin[index] != "None":
                node.left = TreeNode(int(strin[index]))
                queue.append(node.left)
            index += 1

            if strin[index] != "None":
                node.right = TreeNode(int(strin[index]))
                queue.append(node.right)
            index += 1
        
        return root

"""
Practice, my try:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            one_check = 0
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                    one_check += 1
                else:
                    result.append(None)
                    queue.append(None)
                    queue.append(None)
            if not one_check: break
        return ",".join(str(item) for item in result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        result = []
        strin = data.split(",")

        index = 0
        dummy = TreeNode(0)
        curr = dummy.left
        for x in range(len(strin)):
            if strin[x] == None:
                continue
            val = int(strin[x])
            if not curr:
                curr = TreeNode(val)
            if strin[2*x + 1] == None:
                continue
            vall = int(strin[2*x + 1])
            curr.left = TreeNode(vall)

            if strin[2*x + 2] == None:
                continue
            valr = int(strin[2*x + 2])
            curr.right = TreeNode(valr)

            if (x + 1) % 2 == 1

"""