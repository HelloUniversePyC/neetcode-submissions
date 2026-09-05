class Solution:
    def maxArea(self, heights: List[int]) -> int:
      def get_area(left: int, right: int) -> int:
        return min(heights[left], heights[right])*(right-left)
      left, right = 0, len(heights) -1
      max_area = -float('inf')
      while left < right:
        if heights[right] <= heights[left] and get_area(left, right) <= max_area:
            right-=1
        elif heights[right] > heights[left] and get_area(left, right) <= max_area:
            left+=1
        max_area = max(get_area(left, right), max_area)
      return max_area

        
        