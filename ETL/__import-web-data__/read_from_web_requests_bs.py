# Import packages
import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extracts the response as html: html_doc
html_doc = r.text
# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc,features="html.parser")

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()
#print(pretty_soup)

# Get the title of Guido's webpage: guido_title
guido_title = soup.title
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()
print(guido_text)

# Find all 'a' tags (which define hyperlinks): a_tags #### hyperlinks are defined by the HTML tag <a>
a_tags = soup.find_all('a')
for link in a_tags:
    print(link.get('href'))

