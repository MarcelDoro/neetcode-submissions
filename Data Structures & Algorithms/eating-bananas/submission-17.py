class Solution:
    def ceildiv(self, a, b):
        return -(a // -b)

    def canEat(self, p: List[int], h: int, s: int) -> bool:
        time = 0
        for i in range(len(p)):
            time += self.ceildiv(p[i], s)
            if time > h:
                return False

        return True
                
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        print(int(2 / 5))
        mini = 1
        maxi = 0
        for p in piles:
            if p > maxi:
                maxi = p
        
        while mini <= maxi:
            cp_piles = piles.copy()
            mid = (mini + maxi) // 2
            if mini == maxi:
                return mini
            elif self.canEat(cp_piles, h, mid) == True:
                maxi = mid
            else:
                mini = mid + 1

