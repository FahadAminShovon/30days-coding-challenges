

    def getHeight(self,root):
        if root == None:
            return -1
        a = self.getHeight(root.left)
        b = self.getHeight(root.right)
        return 1+max(a,b)
        

