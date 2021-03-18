class Solution(object):
    def remove_vowels(self,string):
        vowels=['a','e','i','o','u']
        for x in string.lower():
            if x in vowels:
                string = string.replace(x,"")

        print(string)

if __name__  == "__main__":
    a = Solution()
    a.remove_vowels("keerthana")