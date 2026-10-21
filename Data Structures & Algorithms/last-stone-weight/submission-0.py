class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            
            stones.sort()
            
            y = stones.pop() # heaviest stone
            x = stones.pop() # 2nd heaviest stone
            
            if x != y:
                stones.append(y - x)
                
        if stones:
            return stones[0]
        else:
            return 0
            