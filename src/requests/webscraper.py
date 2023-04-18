import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)

content_web_page = response.text

soup = BeautifulSoup(content_web_page, "html.parser")

article_texts = []

article_texts = soup.find_next_siblings('//span[@class="titleline"]//a')

print(article_texts)

for li in article_texts:
    # txt = li.split()[1]
    print(li)

# //span[@class='titleline']//a
