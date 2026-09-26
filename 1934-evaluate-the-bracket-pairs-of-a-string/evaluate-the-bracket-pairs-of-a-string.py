class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge = dict(knowledge)

        res = []
        i = 0

        while i < len(s):

            if s[i] == "(":
                i += 1
                start = i

                while s[i] != ")":
                    i += 1

                key = s[start:i]
                res.append(knowledge.get(key, "?"))

                i += 1

            else:
                start = i

                while i < len(s) and s[i] != "(":
                    i += 1

                res.append(s[start:i])

        return "".join(res)