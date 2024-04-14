class DynamicArray:
    def __init__(self):
        self.array = [0] * 2
        # keep track of the where the last item in the array is
        # used for adding and removing items from the array
        self.currentIndex = 0
        self.capacity = 2

    def add(self, item):
        if (self.currentIndex == self.capacity):
            self.resizeArray()
        self.array[self.currentIndex] = item
        self.currentIndex += 1

    def remove(self):
        if (self.currentIndex == 0):
            raise Exception("Cannot remove from empty list")
        self.currentIndex -= 1

    def resizeArray(self):
        # expensive operation
        self.capacity *=2
        newArr = [0] * self.capacity
        for i in range (len(self.array)):
            newArr[i] = self.array[i]
        self.array = newArr
    
    def get(self, index):
        if index < 0 or index >= self.currentIndex:
            raise IndexError("Index out of bounds!")
        return self.array[index]

    def size(self):
        return self.currentIndex
    
my_array = DynamicArray()
my_array.add(10)
my_array.add(20)
my_array.add(30)

print(my_array.get(0))  # Output: 10
print(my_array.size())  # Output: 3

my_array.remove()
print(my_array.size())  # Output: 2



