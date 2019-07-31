import json, requests, time
from bs4 import BeautifulSoup

# 保存已经抓取和未抓取的链接

visited_urls = []
unvisited_urls = ["https://www.chainnews.com/"]

# 从队列中访问一个未抓取的链接

def get_unvisited_urls():
    while True:
        if len(unvisited_urls) == 0:
            return None
        
        url = unvisited_urls.pop()

        if url in visited_urls:
            continue
        
        visited_urls.append(url)
        return url

if __name__ == "__main__":

    while True:
        url = get_unvisited_urls()
        if url == None:
            break
        
        response = requests.get(url)
        content = response.content.decode('utf-8')
        #print(content)

        soup = BeautifulSoup(content,"html.parser")
        # 获取当前页面的所有链接
        
        for element in soup.select("a"):
            if not element.has_attr("href"):
                continue
            if not element["href"].startswith("https://"):
                continue
            print(element["href"])
        
        time.sleep(1)