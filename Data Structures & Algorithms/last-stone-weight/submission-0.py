import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-stone for stone in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) > 1:
            stone_1 = stones_heap[0] 
            stone_2 = heapq.nsmallest(2, stones_heap)[-1]
            if stone_1 == stone_2:
                stones_heap.remove(stone_1)
                stones_heap.remove(stone_2)
            elif stone_1 < stone_2:
                stones_heap[0] = stones_heap[0] + (-stone_2)
                stones_heap.remove(stone_2)
                
            else:
                stones_heap.remove(stone_1)
                stones_heap.remove(stone_2)
                stones_heap.append(stone_2 + -(stone_1))
            heapq.heapify(stones_heap)
        return 0 if not stones_heap else -stones_heap[0]


        
        