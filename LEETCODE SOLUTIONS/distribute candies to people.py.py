distribute candies to people.py


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        count, ans = 0, [0] * num_people
        while candies > 0:
            ans[count % num_people] += min(candies, count + 1)
            candies -= count + 1
            count += 1
        return ans