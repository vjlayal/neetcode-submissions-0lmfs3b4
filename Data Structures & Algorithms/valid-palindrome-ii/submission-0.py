class Solution(object):

    def check(self, s , i , j):
        while i<j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True

    def validPalindrome(self, s):
        i,j = 0, len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return self.check(s, i+1, j) or self.check(s, i, j-1)
        return True
        