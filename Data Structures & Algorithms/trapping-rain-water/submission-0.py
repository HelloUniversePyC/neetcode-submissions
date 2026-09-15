class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall =r_wall = 0
        len_elevs = len(height)
        max_l = [0]*len_elevs #prefix array of max wall to left of i
        max_r = [0]*len_elevs #suffix array of max wall to right of i

        for i in range(len_elevs):
            j = -i -1 #allow us to go backward
            max_l[i] = l_wall
            max_r[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        
        total_water = 0
        for i in range(len_elevs):
            trap = min(max_l[i], max_r[i])
            total_water+=max(0, trap-height[i])
        return total_water





            