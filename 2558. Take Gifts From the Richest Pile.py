class Solution(object):
    def pickGifts(self, gifts, k):
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            remaining = int(math.sqrt(largest))
            heapq.heappush(max_heap,-remaining)
        return -sum(max_heap)

        