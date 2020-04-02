from modules import *

def load_page(url):

    headers={'User-Agent':'''Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0''',
             'Accept':'''text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
             'Connection':'''keep-alive'''}

    req = ur.Request(url=url, headers=headers)

    return ur.urlopen(req)


def url_normalize(cur_page, path):       #Quoting/Encoding/Decoding URLs left

    cur_page=cur_page.strip()
    path=path.strip()

    a=list(up.urlparse(cur_page))
    b=list(up.urlparse(path))

    if b[2]=='':
        return None

    b[2] = up.quote(b[2], safe=';/?:@&=+$,')

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

        b[0]=a[0]
        b[1]=a[1]

        if b[2][0]=='/':    #search in 'root' directory

            return up.urlunparse(b)

        if b[2][0:2] == './' or (b[2][0] not in ['/', '.']):  # search in the same directory
            a[2] = remove_fname(a[2])

            if b[2][0] == '.':
                b[2] = b[2][1:]

            if b[2][0] != '/':
                b[2] = '/' + b[2]

            b[2] = a[2] + b[2]

            return up.urlunparse(b)


        if b[2][:3]=='../' or b[2][:5]=='./../':    #search in previous directory
            a[2]=remove_fname(remove_fname(a[2]))

            if b[2][:3]=='../':
                b[2]=b[2][2:]

            else:
                b[2]=b[2][4:]

            b[2] = a[2] + b[2]
            return up.urlunparse(b)


        print("****",path,"****")
        return None




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


def remove_fname(s):
    if s=='':
        return ''

    i=len(s)-1

    while i>=0 and s[i]!='/':
        i-=1

    if i==-1:
        return ''

    else:
        return s[:i]


def target_test(url):
    pass


