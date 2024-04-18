
import urllib.request as req, bs4

############## fetch data ##############

titles_list = []
likeCounts_list = []
articalUrls_list = []
dateTimes_list = []
def getData(url):
    request = req.Request(url, headers={
        "User-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
        "cookie":"over18=1"
    })
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')
    
    root = bs4.BeautifulSoup(data, "html.parser")
    ### parsing rules
    titles = root.find_all("div", class_="title") # 尋找所有 class="title"的div標籤
    for title in titles:
        if  title.a != None:
            # print(type(title)) # bs4.element.Tag
            # <div class="title"><a href="/bbs/Lottery/M.1713107630.A.6BB.html">[討論] 2024.04.13 開獎結果</a></div>
            # print(title.a.string+","+title.a['href'])
            titles_list.append(title.a.string)
            articalUrls_list.append("https://www.ptt.cc"+title.a['href'])
            
        else:
            # 使用strip把空白(\t\n\r)刪除  ref:https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string
            # print(title.string.strip()+","+"no link")
            titles_list.append(title.string.strip())
            articalUrls_list.append("") # no link


    likeCounts = root.find_all("div", class_="nrec")
    for likeCount in likeCounts:
        if likeCount.span != None:
            # print(likeCount.span.string)
            likeCounts_list.append(likeCount.span.string)
        else:
            # print("no count")
            likeCounts_list.append("") # no count
    
    ### nextLink
    nextLink = root.find("a", string="‹ 上頁")
    return "https://www.ptt.cc"+nextLink["href"]

def getArticleDateTime(url):

    if(url==""):
        dateTimes_list.append("") # no date/time
        return
    
    request = req.Request(url, headers={
        "User-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
        "cookie":"over18=1"
    })
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')
    
    root = bs4.BeautifulSoup(data, "html.parser")

    # 透過觀察得到時間欄位的css選取規則
    dateTime = root.select(".article-metaline+ .article-metaline .article-meta-value")
    # print(type(dateTime)) # bs4.element.ResultSet
    # [<span class="article-meta-value">Sun Apr 14 23:13:46 2024</span>]
    
    if(len(dateTime)==0):
        dateTimes_list.append("") # no date/time
        return
    # print(dateTime[0].string)
    
    # print(dateTime.string)
    # print(root.find(dateTime).span.string)
    dateTimes_list.append(dateTime[0].string)
    # 也可以用find_all(class_="article-meta-value") 再找出最後一個即為時間資訊 # 暫不實做
    # article_metas = root.find_all("span", class_="article-meta-value")
    # for meta in article_metas:
    #   ...


pageUrl = "https://www.ptt.cc/bbs/Lottery/index.html"
count = 0
while count < 3:
    pageUrl = getData(pageUrl)
    count += 1
# print(pageUrl)

# print(titles_list)
# print(likeCounts_list)
# print(articalUrls_list)


for url in articalUrls_list:
    getArticleDateTime(url)

# print(dateTimes_list)

result = []
for title,likeCount,dateTime in zip(titles_list, likeCounts_list, dateTimes_list):
    row = [title, likeCount, dateTime]
    # row = [title+","+likeCount+","+dateTime]
    # print(row)
    result.append(row)
# print(result)

### output
import csv
# header = ["title","likeCount","dateTime"]
with open("article.csv", "w", encoding="cp950", newline="") as f:
    writer = csv.writer(f)
    # writer.writerow(header) 
    writer.writerows(result)
