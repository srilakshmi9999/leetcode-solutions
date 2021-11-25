duplicate zeroes.py


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        shift, n = 0, len(arr)
        for x in arr:
            if x == 0:
                shift += 1
        
        for i in range(n - 1, -1, -1):
            if i + shift < n:
                arr[i + shift] = arr[i]
            if arr[i] == 0:
                shift -= 1
                if shift + i < n:
                    arr[shift + i] = arr[i]