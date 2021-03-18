class Solution(object):
    def rev_string(self, x):
        str_1 = list(x)
        str_2 = str_1[::-1]
        str_3 = ''.join(str_2)
        print(str_3)

if __name__ == "__main__":
    a = Solution()
    a.rev_string("keer")
