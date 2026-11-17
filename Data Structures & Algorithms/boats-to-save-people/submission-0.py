class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        minimum_boats = 0
        people.sort()
        r = len(people) - 1
        l = 0
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            minimum_boats+=1
        if l == r:
            minimum_boats += 1
        return minimum_boats