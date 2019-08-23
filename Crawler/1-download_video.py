import requests, re

response = requests.get("https://www.meipai.com/media/1134583495")
print(response.text)


# response = requests.get(
#     "http://mvvideoshare2.meitudata.com/5d4d62647f13easbs54wcl6247_H264_MP5d4e0c.mp4")
#
# with open("./meipai_video/1.mp4", mode='wb') as f:
#     f.write(response.content)
