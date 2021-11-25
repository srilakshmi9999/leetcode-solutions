convert to base-2


class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        ans = []
        while N != 0:
            reminder = N % -2
            N //= -2
            if reminder < 0:
                reminder += 2
                N += 1
            ans.append(str(reminder))
        
        if len(ans) == 0:
            return "0"
        else:
            # Attetion here:
            # list.reverse() method acts in-place, and therefore returns None
            # "".join(ans.reverse()) will be wrong (can't be iterable)
            ans.reverse()
            return "".join(ans)