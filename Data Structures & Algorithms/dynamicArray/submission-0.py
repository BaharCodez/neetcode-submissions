class DynamicArray:
    
    def __init__(self, capacity: int):
        array = [] * self.capacity


    def get(self, i: int) -> int:
        return self.array.get[i]


    def set(self, i: int, n: int) -> None:
        self.array.set[i]


    def pushback(self, n: int) -> None:
        self.array.append[n]

    def popback(self) -> int:
        return self.array.pop()
 
    def resize(self) -> None:
        self.array = self.array * 2 


    def getSize(self) -> int:
        return len(self.array)
        
    
    def getCapacity(self) -> int:
        self.array.get.capacity()
