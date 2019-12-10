import requests
from bs4 import BeautifulSoup

keywords = BeautifulSoup(requests.get("https://www.daum.net").text, "html.parser").select('[class=txt_issue]') 
[word.text for word in keywords][::2]
