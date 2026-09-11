from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        used = [False] * n
        seen = set()

        def backtrack(num):
            if len(num) == 3:
                if num[-1] % 2 == 0:
                    seen.add(tuple(num))
                return

            for ind in range(n):
                if used[ind]:
                    continue

                if len(num) == 0 and digits[ind] == 0:
                    continue

                used[ind] = True
                num.append(digits[ind])

                backtrack(num)

                num.pop()
                used[ind] = False

        backtrack([])
        return len(seen)