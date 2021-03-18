class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        water = 0
        head = 0
        tail = len(height) - 1

        for cnt in range(len(height)):

            width = abs(head - tail)
            print(width)

            if height[head] < height[tail]:
                res = width * height[head]
                #print(res)
                head += 1

            else:
                res = width * height[tail]
                tail -= 1

            if res > water:
                water = res

        return water


if __name__ == "__main__":
    a = Solution()
    print(a.maxArea([1,8,6,2,5,4,8,3,7]))