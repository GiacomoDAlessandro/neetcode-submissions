class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0, len(people) - 1
        boats = 0

        while l <= r:
            total = people[l] + people[r]
            if total > limit:
                boats += 1
                r -= 1
            elif total == limit:
                boats += 1
                r -= 1
                l += 1
            #Two weigh less together than the limit try adding one more
            else:
                l += 1
                r -= 1
                while total < limit and l >= 0:
                    print(l, r, boats)
                    total += people[l]
                boats += 1

        return boats