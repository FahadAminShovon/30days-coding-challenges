

    def removeDuplicates(self,head):
        #Write your code here
        curr = head
        while curr:
            temp  = curr
            if curr.next:
                while temp.next.data == temp.data :
                    temp = temp.next
                    if temp.next == None:
                        break
            curr.next = temp.next
            curr=curr.next

        return head

