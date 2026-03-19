class Solution:
    def countAndSay(self, n: int) -> str:
        def change(n):
            s = ''
            l = 1
            for j in range(1,len(n)):
                if n[j] == n[j-1]:
                    l+=1
                else:
                    s += str(l)
                    s += n[j-1]
                    l = 1
            s += str(l)
            s += n[len(n)-1]
            return s
        res = '1'
        for i in range(n-1):
            res = change(res)
        return res
                