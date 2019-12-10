import requests
from bs4 import BeautifulSoup

keywords = BeautifulSoup(requests.get("http://zum.com").text, 
                         "html.parser").select('[class="keyword d_keyword"]') 
[word.text for word in keywords][::2]
