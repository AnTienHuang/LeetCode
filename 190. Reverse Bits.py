# 190. Reverse Bits
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)
        return int(binary[::-1], 2)