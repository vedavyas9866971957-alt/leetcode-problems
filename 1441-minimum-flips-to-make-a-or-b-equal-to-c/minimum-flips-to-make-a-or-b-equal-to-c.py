class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]

        n = max(len(a), len(b), len(c))

        a = a.zfill(n)
        b = b.zfill(n)
        c = c.zfill(n)

        count = 0

        for i in range(n):
            x = int(a[i])
            y = int(b[i])
            z = int(c[i])

            if (x | y) == z:
                continue

            if z == 1:
                count += 1
            else:
                count += x + y

        return count