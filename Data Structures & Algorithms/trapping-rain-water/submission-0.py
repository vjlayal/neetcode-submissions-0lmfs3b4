class Solution(object):
    def trap(self, height):
        n = len(height)
        l,r = 0, n-1
        lMax, rMax = height[l], height[r]
        water = 0
        while l<=r:
            if lMax<rMax :
                lMax = max(lMax, height[l])
                water += lMax-height[l]
                l+=1
            else:
                rMax = max(rMax, height[r])
                water += rMax-height[r]
                r-=1
        return water
        