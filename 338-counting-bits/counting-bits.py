class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for x in range(n+1):
            c=0
            i=x
            while i!=0:
                if (i&1)==1:
                    c+=1
                i=i>>1
            ans.append(c)
        return ans
        