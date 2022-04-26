class Heap:
    def __init__(self) -> None:
        self.h: list[float] = []
        self.heap_size: int = 0

    def parent_index(self, child_idx: int) -> int | None:
        """return the parent index of given child"""
        if child_idx > 0:
            return (child_idx - 1) // 2
        return None

    def left_child_idx(self, parent_idx: int) -> int | None:
        """
        return the left child index if the left child exists.
        if not, return None.
        """
        left_child_index = 2 * parent_idx + 1
        if left_child_index < self.heap_size:
            return left_child_index
        return None

    def right_child_idx(self, parent_idx: int) -> int | None:
        """
        return the right child index if the right child exists.
        if not, return None.
        """
        right_child_index = 2 * parent_idx + 2
        if right_child_index < self.heap_size:
            return right_child_index
        return None

    def max_heapify(self, index: int) -> None:
        """
        correct a single violation of the heap property in a subtree's root.
        """
        if index < self.heap_size:
            violation: int = index
            left_child = self.left_child_idx(index)
            right_child = self.right_child_idx(index)
            # check which child is larger than its parent
            if left_child is not None and self.h[left_child] > self.h[violation]:
                violation = left_child
            if right_child is not None and self.h[right_child] > self.h[violation]:
                violation = right_child
            # if violation indeed exists
            if violation != index:
                # swap to fix the violation
                self.h[violation], self.h[index] = self.h[index], self.h[violation]
                # fix the subsequent violation recursively if any
                self.max_heapify(violation)

    def build_max_heap(self, collection: Iterable[float]) -> None:
        """build max heap from an unsorted array"""
        self.h = list(collection)
        self.heap_size = len(self.h)
        if self.heap_size > 1:
            # max_heapify from right to left but exclude leaves (last level)
            for i in range(self.heap_size // 2 - 1, -1, -1):
                self.max_heapify(i)

    def max(self) -> float:
        """return the max in the heap"""
        if self.heap_size >= 1:
            return self.h[0]
        else:
            raise Exception("Empty heap")

    def extract_max(self) -> float:
        """get and remove max from heap"""
        if self.heap_size >= 2:
            me = self.h[0]
            self.h[0] = self.h.pop(-1)
            self.heap_size -= 1
            self.max_heapify(0)
            return me
        elif self.heap_size == 1:
            self.heap_size -= 1
            return self.h.pop(-1)
        else:
            raise Exception("Empty heap")

    def insert(self, value: float) -> None:
        """insert a new value into the max heap"""
        self.h.append(value)
        idx = (self.heap_size - 1) // 2
        self.heap_size += 1
        while idx >= 0:
            self.max_heapify(idx)
            idx = (idx - 1) // 2

    def heap_sort(self) -> None:
        size = self.heap_size
        for j in range(size - 1, 0, -1):
            self.h[0], self.h[j] = self.h[j], self.h[0]
            self.heap_size -= 1
            self.max_heapify(0)
        self.heap_size = size