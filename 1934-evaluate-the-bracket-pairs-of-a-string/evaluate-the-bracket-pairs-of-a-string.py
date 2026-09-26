class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hashknowledge=dict(knowledge)

        res=[]
        i=0
        while(i<len(s)):
            char=s[i]
            if char=="(":
                key=""
                i+=1
                while(s[i]!=")"):
                    key+=s[i]
                    i+=1
                res.append(hashknowledge.get(key,"?"))
                i+=1
            else:
                st=[]
                while(i<len(s) and s[i]!="("):
                    st.append(s[i])
                    i+=1
                res.append("".join(st))
        return  "".join(res)
            