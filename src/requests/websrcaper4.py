import requests
from lxml.html import fromstring

r = requests.get('https://www.rottentomatoes.com/m/leto')
root = fromstring(r.text)

print(root)

# directed = root.xpath("//*[contains(.,'Directed By')]/parent::*/*[@class='meta-value']/a/text()")
# written = root.xpath("//*[contains(.,'Written By')]/parent::*/*[@class='meta-value']/a/text()")
# written_links = root.xpath(".//*[contains(.,'Written By')]/parent::*/*[@class='meta-value']/a//@href")
# print(directed, written, written_links)
