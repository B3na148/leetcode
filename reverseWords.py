class Solution:
    def reverseWords(self, s: str) -> str:
        #while its not the fastest way to do it, i think its a nice managment of complexity.
        count = 0
        mat = []
        mat.append([])
        for i in s:
            if i == " ":
                if mat[count]:
                    mat.append([])
                    count += 1
            else:
                mat[count].append(i)
        if len(mat[-1]) == 0:
            mat.pop()
        finle = ""
        for i in range(len(mat) - 1, -1, -1):
            finle += "".join(mat[i])
            finle += " "
        finle = finle[:-1]
        return finle
