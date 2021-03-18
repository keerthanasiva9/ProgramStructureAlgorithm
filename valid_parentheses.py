class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brac = ['{', '[', '(']
        closed_brac = ['}', ']', ')']

        # dicts = {"(":")","{":"}","[":"]"}

        op = []

        for i in s:
            if i in open_brac:
                op.append(i)

            elif i in closed_brac:
                pos = closed_brac.index(i)
                if open_brac[pos] == op[len(op) - 1]:
                    op.pop()

                else:
                    return False

        if len(op) == 0:
           return True
        else:
           return False

if __name__ == "__main__":
    a = Solution()
    print(a.isValid("([)]"))