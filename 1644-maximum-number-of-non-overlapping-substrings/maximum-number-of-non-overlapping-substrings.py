class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = {}
        last = {}

        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []

        for c in first:
            start = first[c]
            end = last[c]

            i = start
            valid = True

            while i <= end:
                ch = s[i]

                # This character appeared before start,
                # so we cannot create a valid substring
                # beginning at start.
                if first[ch] < start:
                    valid = False
                    break

                # Expand the interval if needed.
                end = max(end, last[ch])
                i += 1

            if valid:
                intervals.append((start, end, s[start:end + 1]))

        # Sort by ending index
        intervals.sort(key=lambda x: x[1])

        result = []
        last_end = -1

        for start, end, sub in intervals:
            if start > last_end:
                result.append(sub)
                last_end = end

        return result