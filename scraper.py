import requests
from bs4 import BeautifulSoup

response = requests.get("https://oxylabs.io/")
print(response.text)


url = "https://oxylabs.io/blog"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)