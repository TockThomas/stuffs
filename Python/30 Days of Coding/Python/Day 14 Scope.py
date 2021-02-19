class Difference:
    def __init__(self, a):
        self.__elements = a
        self.differences = [0]
        
    def computeDifference(self):
        self.__elements.sort(reverse=True)

        for i in self.__elements:
            for j in self.__elements:
                if i > j:
                    x = i - j
                    self.differences.append(x)
        self.differences.sort(reverse=True)
        self.maximumDifference = self.differences[0]

# End of Difference class