

    def levelOrder(self,root):
        queue = [root] if root else []

        while queue:
            temp = queue.pop()
            print(temp.data,end=" ")

            if temp.left: queue.insert(0,temp.left)
            if temp.right: queue.insert(0,temp.right)



