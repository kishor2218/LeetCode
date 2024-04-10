# for inputing number.then results in boolean

class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        if y<0:
            return false
        else:
            return y==y[::-1]
