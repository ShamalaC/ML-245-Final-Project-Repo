class TwoPowerXHeap:
    def __init__(self, x):
        self.x = x
        self.heap = []

    def parent(self, i):
        return (i - 1) // (2 ** self.x)

    def first_child(self, i):
        return (2 ** self.x) * i + 1

    def insert(self, value):
        # Append the new value at the end of the heap
        self.heap.append(value)
        # Bubble up to maintain heap property
        self._bubble_up(len(self.heap) - 1)

    def pop_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # The root is the max element
        max_value = self.heap[0]
        # Move the last element to the root and remove the last element
        self.heap[0] = self.heap.pop()
        # Bubble down to maintain heap property
        self._bubble_down(0)
        
        return max_value

    def _bubble_up(self, index):
        while index > 0:
            parent_index = self.parent(index)
            if self.heap[index] > self.heap[parent_index]:
                # Swap the current element with its parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _bubble_down(self, index):
        while True:
            first_child_index = self.first_child(index)
            max_index = index

            for i in range(2 ** self.x):
                child_index = first_child_index + i
                if child_index < len(self.heap) and self.heap[child_index] > self.heap[max_index]:
                    max_index = child_index

            if max_index == index:
                break

            # Swap the current element with the largest child
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            index = max_index

# Example Usage
heap = TwoPowerXHeap(x=3)  # This means each node has 2^3 = 8 children
heap.insert(10)
heap.insert(20)
heap.insert(15)
heap.insert(30)

print(heap.pop_max())  
print(heap.pop_max()) 
