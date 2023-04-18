import bs4

soup = bs4.BeautifulSoup("""
<span class="price">Price including shipping:</span>
<span>83.13</span>
""", "html.parser")

# using find() method:
soup.find('span', class_="price").find_next_sibling('span').text
# "83.13"

# using CSS selectors and `~` notation:
print(soup.select('.price ~ span')[0].text)
# or
print(soup.select_one('.price ~ span').text)
# "83.13"
