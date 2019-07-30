import json, requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    response = requests.get("https://www.chainnews.com/")
    content = response.content.decode('utf-8')
    #print(content)

    soup = BeautifulSoup(content,"html.parser")
    # 获取当前页面的所有链接
    