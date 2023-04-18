import bs4
import requests

url = "https://news.ycombinator.com/"

response = requests.get(url)

content_web_page = response.text

soup = bs4.BeautifulSoup(content_web_page, "html.parser")

# print(soup)

article_texts_ = []

article_texts = soup.find_all('span', class_="titleline")

for item in article_texts:
    link = item.find_next('a').getText()
    article_texts_.append(link)
    # print(link)

print(len(article_texts_))
