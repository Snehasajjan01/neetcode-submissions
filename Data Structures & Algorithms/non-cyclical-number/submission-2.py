class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            curr_sum = 0
            while n > 0:
                last_digit = n % 10
                curr_sum += last_digit ** 2
                n = n // 10
            n = curr_sum
        return True

            




        