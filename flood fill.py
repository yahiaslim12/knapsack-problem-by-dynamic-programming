import numpy as np
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        if  oldColor == color:
            return image
        def dfs(image,sr,sc):
            
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != oldColor:
                return
            image[sr][sc] = color
            dfs(image,sr-1,sc)
            dfs(image,sr+1,sc)
            dfs(image,sr,sc-1)
            dfs(image,sr,sc+1)
        dfs(image,sr,sc)
        return image
sol = Solution()
image = np.array([[1,1,1],[1,1,0],[1,0,1]])
res = sol.floodFill(image,1,1,2)
print(res)

        




        
         
        
    
        
            




