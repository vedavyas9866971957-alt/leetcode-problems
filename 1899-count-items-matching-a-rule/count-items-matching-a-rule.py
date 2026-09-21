class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        x = 0

        if ruleKey == "type":
            x = 0
        elif ruleKey == "color":
            x = 1
        else:
            x = 2

        value = 0

        for i in items:
            if i[x]==ruleValue:
                value = value + 1

        return value
        