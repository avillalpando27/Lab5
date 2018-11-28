class Heap:

    def __init__(self):
        self.heap_array = []
        self.current_size = 0

    def percolate_up(self, index, size): # method percolates the minimum value up after each insertion

        current = (2 * index) + 1
        value = self.heap_array[index]

        while current < size:
            min = value
            min_index = -1
            i = 0
            while i < 2 and i + current < size:
                if self.heap_array[i + current] < min:
                    min = self.heap_array[i + current]
                    min_index = i + current
                i += 1

            if min == value:
                return

            temp = self.heap_array[index]
            self.heap_array[index] = self.heap_array[min_index]
            self.heap_array[min_index] = temp



    def insert(self, k): # the breadth of this method is done by the percolate method, which ensures MinHeap properties

        self.heap_array.append(k)
        self.current_size += 1
        for i in range(len(self.heap_array)):
            self.percolate_up(i, self.current_size)

    def percolate_down(self, index): # method percolates larger numbers down when each min root is "extracted"

        while (index * 2) < self.current_size:
            if index * 2 + 1 > self.current_size:
                minChild = index * 2
            else:
                if self.heap_array[index * 2 + 1] < self.heap_array[index * 2 + 2]: # chooses the smaller child of the two
                    minChild = (index * 2) + 1
                else:
                    minChild = (index * 2) + 2

            if self.heap_array[index] > self.heap_array[minChild]: # swaps actual values when min heap properties have been violated
                temp = self.heap_array[index]
                self.heap_array[index] = self.heap_array[minChild]
                self.heap_array[minChild] = temp
            index = minChild



    def extract_min(self):

        if self.is_empty():
            return None

        min_elem = self.heap_array[0]
        self.heap_array[0] = self.heap_array[self.current_size-1]
        self.current_size = self.current_size - 1
        self.percolate_down(0)

        return min_elem

    def is_empty(self):
        return len(self.heap_array) == 0

    def heapSort(self): # method returns a new list with the values now sorted
        result = []
        while self.current_size != 0:
            currMin = self.extract_min()
            result.append(currMin)

        return result

    def print_heap(self):
        print(self.heap_array)