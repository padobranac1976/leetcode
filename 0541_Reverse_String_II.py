class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left = 0
        right = k-1
        output = ""
        while left <= len(s) - 1:
            right = min(right, len(s)-1)
            while right >= left:
                output += s[right]
                right -= 1
            left += k
            right = left + k - 1
            
            while right >= left:
                if left > len(s) - 1:
                    break
                output += s[left]
                left += 1
            right = left + k -1
        return output
    
s = "abcdefg"
k = 2
obj = Solution()
print(obj.reverseStr(s, k))