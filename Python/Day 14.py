

    # Add your code here
    def computeDifference(self):
        sz = len(self.__elements)
        l = []
        for i in self.__elements:
            for j in range(sz):
                xx = i-self.__elements[j]
                l.append(abs(xx))
        l.sort()
        self.maximumDifference = l[len(l)-1]



