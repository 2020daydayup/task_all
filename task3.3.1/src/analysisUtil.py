from src.logg import get_log
from bs4 import BeautifulSoup
import jieba
import collections
import requests
import json

url = "https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98&" \
      "productId=100012015170&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"

data = requests.get(url)
print(type(data.text))