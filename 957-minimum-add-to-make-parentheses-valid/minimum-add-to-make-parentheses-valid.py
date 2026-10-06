class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o=0
        c=0
        add=0
        for ch in s:
            if ch=="(":
                o+=1
            else:
                c+=1
                if c>o:
                    add+=1
                    o=0
                    c=0
        if o-c>0:
            add+=o-c
        return add
