class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        list_or = []
        dic1={}
        for i in range(s.__len__()):
            list_or.append(s[i])
            dic1[s[i]]=1

        maxoddcnt=0
        result=0
        for k in dic1.keys():
            cnt=list_or.count(k)
            
            if(cnt%2 == 0):
                result = result+cnt
            else:
                maxoddcnt = max(maxoddcnt,cnt)
                result = result + cnt -1
        
        if maxoddcnt > 0:
            result = result + 1
        print('longestPalindrome of {} is:{}'.format(s,result))
        return result

