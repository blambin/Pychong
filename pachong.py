
import re
import urllib.request
import urllib
import http.cookiejar
import pickle


from collections import deque

def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


def savefile(data):
    save_path = './sav_dat.txt'
    f_obj = open(save_path,'w')

    pickle.dump(data,f_obj)
    f_obj.close()



# 爬虫开始
queue = deque()
visited = set()

url = "http://wordpress.org/"  #入口页面

queue.append(url)
cnt = 0

#需要保存的项目



# 爬虫循环开始
while queue:
    url = queue.popleft()
    visited |= {url}

    print('已经抓取: ' + str(cnt) + ' 正在抓取 <-- ' + url)
    cnt += 1
    
    openr = makeMyOpener() # 创建打开器

    try:
        urlop = openr.open(url,timeout = 1000)

    except Exception as ex :
        print(ex)
        continue

    if 'html' not in urlop.getheader('Content-Type'):
        continue


    #尝试编码，出错了继续
    try:
        data = urlop.read().decode('UTF-8')
    except:
        continue

    #正则

    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            #print(queue)
            print('把 '+ x + "加入队列。")

    #保存结果
    
    #save_list = [queue,visited]
    #savefile(save_list)

#循环结束


    


    
