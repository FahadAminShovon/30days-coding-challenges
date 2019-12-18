

    def insert(self,head,data): 
    #Complete this method
        n = Node(data)
        if (head==None):
            self.head = n
            return self.head

        curr = self.head
        while(curr.next!=None):
            curr=curr.next
        curr.next = n
        return self.head
                    

