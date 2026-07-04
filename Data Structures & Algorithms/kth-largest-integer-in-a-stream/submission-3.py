class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # min heap
        # then the Kth largest would be the smallest of K numbers
        self.heap = nums
        heapq.heapify(nums)    
        self.k = k

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # at capacity
        if len(self.heap) == self.k:
            if (val < self.heap[0]):
                return self.heap[0]
            heapq.heappop(self.heap)
    
        heapq.heappush(self.heap, val)

        return self.heap[0]