class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palin(s):
            n = len(s)
            for i in range(0,n//2):
                if s[i] != s[n-i-1]:
                    return False
            return True

        lenght = len(s)
        s2 = ""
        for i in range(lenght):
            if 97 <= ord(s[i]) <= 122:
                s2 += s[i]
            if 65 <= ord(s[i]) <= 90:
                s2 += s[i].lower()
            if 48 <= ord(s[i]) <= 57:
                s2 += s[i]

        return is_palin(s2)