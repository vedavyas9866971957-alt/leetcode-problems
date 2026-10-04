class Solution:
    def checkValidString(self, s: str) -> bool:
        # low  = minimum possible number of unmatched '('
        # high = maximum possible number of unmatched '('
        low = 0
        high = 0

        for ch in s:

            if ch == '(':
                # '(' definitely increases the balance
                low += 1
                high += 1

            elif ch == ')':
                # ')' definitely decreases the balance
                low -= 1
                high -= 1

            else:  # ch == '*'
                # '*' can be:
                # ')'  -> balance -1
                # ''   -> balance unchanged
                # '('  -> balance +1
                low -= 1
                high += 1

            # Balance can never be less than 0
            # because a negative balance means more ')' than '('
            low = max(0, low)

            # If even the maximum possible balance is negative,
            # there is no way to make the string valid.
            if high < 0:
                return False

        # For a valid string, we must be able to get balance = 0.
        return low == 0