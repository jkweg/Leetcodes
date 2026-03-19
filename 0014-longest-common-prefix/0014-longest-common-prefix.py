class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min  = 201
        min_str = ""
        for i in range(len(strs)):
            if len(strs[i]) < min:
                min  = len(strs[i])
                min_str = strs[i]
        dlg = 1
        prefix = ""
        while dlg <= min:
            t = min_str[:dlg]
            flag = True
            for i in range(len(strs)):
                if not strs[i][:dlg] == t:
                    flag = False
            if flag:
                prefix = t
            dlg+= 1
        return prefix
                