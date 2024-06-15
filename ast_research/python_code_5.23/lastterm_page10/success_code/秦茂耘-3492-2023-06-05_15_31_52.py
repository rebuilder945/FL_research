class Solution:
    # 返回对应char
    def __init__(self):
        self.stack=[]
    def FirstAppearingOnce(self):
        # write code here
        for e in self.stack:
            if self.stack.count(e)==1:
                return e
        return "None"
    def Insert(self, char):
        # write code here
        self.stack.append(char)

