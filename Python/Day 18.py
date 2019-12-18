

from collections import deque

class Solution:
    # Write your code here
    a = deque()
    b = deque()
    def pushCharacter(self,c):
        self.a.append(c)
    def enqueueCharacter(self,c):
        self.b.appendleft(c)
    def popCharacter(self):
        return self.a.pop()
    def dequeueCharacter(self):
        return self.b.pop()

