import json, requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    response = requests.get("https://www.chainnews.com/")
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
    
    # 获取更多数据

    