import pdb


class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def findStrMode(self, s, m):
        # for s[0] and s[1], m[0] and m[1] are 0
        m.append(0)
        m.append(0)
        # from 2 to len
        psuf = 2
        slen = s.__len__()
        while psuf < slen:
            ppre = m[psuf - 1]
            if ppre == 0 and s[0] != s[psuf - 1]:
                ppre = 0
            else:
                ppre += 1

            if s[ppre] == s[psuf]:
                m.append(ppre)
            else:
                m.append(0)
            psuf += 1
        return m

    def strStr(self, source, target):
        # Write your code here
        slen = source.__len__()
        tlen = target.__len__()
        if tlen == 0:
            return 0

        m = []
        self.findStrMode(target, m)
        ps = 0  # source pointer
        pt = 0  # target pointer
        while ps < slen:
            if source[ps] == target[pt]:
                ps += 1
                pt += 1
            else:
                # source[ps-1] == target[pt-1]
                # source[ps] != target[pt]
                # then is source[ps] == target[next]?
                # find next pt
                if pt < 2:
                    pt = 0
                else:
                    if m[pt - 1] == 0 and target[pt - 1] != target[0]:
                        pt = 0
                        ## source[ps-1] == target[pt-1] != target[0]
                    else:
                        pt = m[pt - 1] + 1

                # compare after pt is update
                if source[ps] == target[pt]:
                    ps += 1
                    pt += 1
                elif pt == 0:
                    ps += 1
                # else: keep ps until pt == 0

            if pt == tlen:
                print('src:{}'.format(source))
                print('tar:{}{}'.format(' ' * (ps - tlen), target))
                print('result is :', (ps - tlen))
                return (ps - tlen)

        print('result is -1')
        return -1

class Solution_rf:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        slen=source.__len__()
        tlen=target.__len__()

        if tlen==0:
            return 0
        
        ps_start = 0
        while ps_start < slen:
            ps = ps_start
            pt = 0
            while ps < slen and pt < tlen:
                if source[ps] == target[pt]:
                    ps += 1
                    pt += 1
                else:
                    break

            if pt == tlen:
                print('rf result is:',ps_start)
                return ps_start
            else:
                ps_start += 1

        print('rf result is -1')
        return -1
        
class Solution1:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def findStrMode(self, s, m):
        # for s[0] and s[1], m[0] and m[1] are 0
        m.append(0)
        m.append(0)
        # from 2 to len
        psuf = 2
        slen = s.__len__()
        while psuf < slen:
            ppre = m[psuf - 1]
            if ppre == 0 and s[0] != s[psuf - 1]:
                ppre = 0
            else:
                ppre += 1

            if s[ppre] == s[psuf]:
                m.append(ppre)
            else:
                m.append(0)
            psuf += 1
        return m

    def strStr(self, source, target):
        # Write your code here
        slen = source.__len__()
        tlen = target.__len__()
        if tlen == 0:
            return 0

        m = []
        self.findStrMode(target, m)
        ps = 0  # source pointer
        pt = 0  # target pointer
        while ps < slen:
            if source[ps] == target[pt]:
                ps += 1
                pt += 1
            else:
                if pt == 0:
                    ps += 1
                else:
                    if pt < 2:
                        pt = 0
                    else:
                        pt=m[pt-1]+1

            if pt == tlen:
                print('src:{}'.format(source))
                print('tar:{}{}'.format(' ' * (ps - tlen), target))
                print('result is :', (ps - tlen))
                return (ps - tlen)

        print('result is -1')
        return -1

src='aaaabbbbcccc'
dst='aabb'

testcase=[
    ('aaaabbbbcccc','aabb'),
    ('abcabcdabcde','abcd'),
    ('abcabadfadfadfjlhdfanvmvniouerkfhjklyuiohjkbnmcdabcdeabcabcdabcde','abcabauerkfhjklyuiohjkbnmcdabcde'),
    ('abcabadfadfadfjlhdfanvmvniouerkfhjkabcdlyuiohjkbnmcdabcdeabcabcdabcde','abcdlyuioh'),
    ('abcdasdfak;kl;kadjljgalkdgjfjdghoiueyyguhghjbnbjnmasdfjkavhbnbcnjhfdjsklfajkfdjk','yyguhghj'),
    ('abcdasdfak;kl;kadjljgalkdgjfjdghoiueyyguhghjbnbjnmasdfjkavhbnbcnjhfdjsklfajkfdjk','njhfdjskldd')
]

t=Solution()
t_rf=Solution_rf()

#''' testcase
tt_cnt=0
cnt=0
for tc in testcase:
    print('testcase:',tc[0],tc[1])
    tt = t.strStr(tc[0],tc[1])
    ttrf = t_rf.strStr(tc[0],tc[1])
    if tt == ttrf:
        tt_cnt +=1

    cnt +=1

print('test cnt:{}, match cnt:{}'.format(cnt,tt_cnt))
#'''
