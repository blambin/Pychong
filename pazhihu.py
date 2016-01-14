#! /usr/bin/env

import gzip
import urllib.request
import http.cookiejar
import re
import time

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

def getXSRF(data):
    cer = re.compile('_xsrf=(.*?);')
    strlist = cer.findall(data)
    return strlist[0]


#-----------------------------------------

url = "http://www.zhihu.com/"
email = 'blambinneng@gmail.com'
password = '********'

openr = makeMyOpener()

urlres = openr.open(url)

resp = urlres.read().decode('utf-8')


zhihuCookie = urlres.getheader("Set-Cookie")

print(getXSRF(zhihuCookie))


_xsrf = getXSRF(zhihuCookie)

#

# 开始用cookie登录
urllogin = url + 'login/email'

#处理验证码开始
getcaptcha = url+'captcha.gif?r='+ str(int(time.time() * 1000))
print(getcaptcha)
logincache = openr.open(getcaptcha)
with open('./captca.gif','wb') as f:
    f.write(logincache.read())

captcha = input("输入登录验证码：")

postDict = {
    '_xsrf':_xsrf,
    'email':email,
    'password':password,
    'remember_me':'true',
    'captcha':captcha,
    }
#处理验证码结束


postData = urllib.parse.urlencode(postDict).encode()
loginRespose = openr.open(urllogin,postData)

#登录成功
loginHtml = loginRespose.read().decode('utf-8')
print("loginHtml is : " + loginHtml)
