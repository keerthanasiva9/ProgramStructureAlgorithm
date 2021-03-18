class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sums = 0

        for i in s:
            if sums == 1 and (i == "V" or i == "X"):
                sums = dicts[i] - 1

            elif sums == 10 and (i == "L" or i == "C"):
                sums = dicts[i] - 10

            elif sums == 100 and (i == "D" or i == "M"):
                sums = dicts[i] - 100

            else:
                sums = sums + dicts[i]
        return sums

if __name__ == "__main__":
    a = Solution()
    print(a.romanToInt("IX"))