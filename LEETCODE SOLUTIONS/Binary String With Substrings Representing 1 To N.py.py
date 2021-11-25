Binary String With Substrings Representing 1 To N.py 

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        return all(bin(i)[2:] in S for i in range(N, N >> 1, -1))
