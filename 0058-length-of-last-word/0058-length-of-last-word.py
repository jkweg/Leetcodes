class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) -1
        lwl = normal = 0
        while i >= 0 :
            if s [i] != " ":
                lwl += 1
            if s[i] == " " and lwl > 0:
                return lwl
            i-= 1
            if i == -1:
                return lwl
        return len(s)