class Integer:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        limit = 1
        while x / limit >= 10:
            limit *= 10
        while x:
            left = x // limit
            right = x % 10
            if left != right:
                return False
            x = (x % limit) // 10
            limit //= 100
        return True

    def reverse(self, x: int) -> int:
        sign = [1,-1][x<0]
        rev, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10)
            rev = rev*10 + mod
        return sign*rev if -pow(2,31) <= sign*rev <= pow(2,31)-1 else 0

print(Integer().reverse(121))
print(Integer().isPalindrome(121))
print(Integer().reverse(12321))
print(Integer().isPalindrome(12321))
print(Integer().reverse(12175121))
print(Integer().isPalindrome(12175121))