class Solution:
    def reverseBits(self, n: int) -> int:
        num=0
        for i in range(32):
            interm=(n&1)
            num=(num<<1)|interm
            n=n>>1
        return num