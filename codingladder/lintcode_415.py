import pdb
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        slen=s.__len__()
        ps=0
        pe=slen-1
        while ps < pe:
            while ps < slen and s[ps].isalnum()==False:
                ps +=1
            while pe >= 0 and s[pe].isalnum()==False:
                pe -=1
            if ps >= pe:
                break
            if s[ps].lower() == s[pe].lower():
                ps +=1
                pe -=1
            else:
                print('result is False')
                return False

        print('result is True')
        return True

testcase=[
    '123abccba321',
    '123a bc cba 32  1',
    '123abcFcba321',
    'asfadfas',
    '.,'
]
t = Solution()
t.isPalindrome(testcase[3])

for tc in testcase:
    t.isPalindrome(tc)