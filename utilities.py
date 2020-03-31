from modules import *

def url_normalize(cur_page, path):

    cur_page=cur_page.strip()
    path=path.strip()

    a=list(up.urlparse(cur_page))

    b=list(up.urlparse(path))

    if b[2]=='':
        return None

    if b[1]!='' and b[1]!=a[1]:   #sub-domain or external site
        s1=extract_domain(a[1])
        s2=extract_domain(b[1])

        if s1==s2:     #sub-domain
            if b[0]=='':
                b[0]='http://'

            return up.urlunparse(b)

        else:        #external site
            return None


    if b[1]=='' or b[1]==a[1]:  #link belonging to the same domain
        a=up.urlunparse(a)
        if a[-1]=='/':     #Processing 'a'
            a=a[:-1]

        if b[2][:3]=='../':

            b[2]=b[2][2:]

            i=-1
            while a[i]!='/':
                i-=1
            a=a[:i]

        else:
            if b[2][:2]=='./':
                b[2]=b[2][1:]

            if b[2][0]!='/':
                b[2] = '/'+b[2]

        return a + b[2]



def extract_domain(s):
    i=len(s)-1

    while i>=0 and s[i]!='.':
        i-=1

    j=0

    while j<i and s[j]!='.':
        j+=1

    if j==i or i==-1:
        return s

    else:
        return s[j+1:]


def target_test(url):
    pass




