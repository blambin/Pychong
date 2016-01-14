
import gzip
import urllib.request
import http.cookiejar

def unzip(data):
    try:
        print('正在解压...')
        data = gzip.decompress(data)
        print('解压完毕.')
    except:
        print('不用解压')

    return data

def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key,value in head.items():
        elem = (key,value)
        header.append(elem)    
    opener.addHeaders = header

    return opener


#-----------------------------------------

openr = makeMyOpener()
print(type(openr))
urlres = openr.open("http://www.zhihu.com/")
resp = urlres.read().decode('utf-8')
print(resp)
