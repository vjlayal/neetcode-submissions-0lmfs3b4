class Solution(object):
    def maxArea(self, height):
        n= len(height)
        i,j = 0, n-1
        area = 0
        while i<j:
            h = min(height[i], height[j])
            w = j-i
            area = max(area, h*w)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return area
        