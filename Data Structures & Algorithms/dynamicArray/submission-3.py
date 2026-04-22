class DynamicArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.capacity = capacity  # The total capacity of the array
        self.size = 0             # The current number of elements in the array
        self.array = [None] * capacity  # The underlying static array

    def get(self, i: int):
        """
        Return the element at index i.
        Assume that index i is valid (0 ≤ i < size).
        """
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        """
        Set the element at index i to n.
        Assume that index i is valid (0 ≤ i < size).
        """
        self.array[i] = n

    def pushback(self, n: int) -> None:
        """
        Push the element n to the end of the array.
        If the array is full, resize it first.
        """
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        """
        Pop and return the element at the end of the array.
        Assume that the array is non-empty.
        """
        if self.size > 0:
            self.size -= 1
            return self.array[self.size]

    def resize(self) -> None:
        """
        Double the capacity of the array.
        """
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        # Using slicing to copy elements
        new_array[:self.size] = self.array[:self.size]
        self.array = new_array
        self.capacity = new_capacity

    def getSize(self) -> int:
        """
        Return the number of elements in the array.
        """
        return self.size

    def getCapacity(self) -> int:
        """
        Return the capacity of the array.
        """
        return self.capacity