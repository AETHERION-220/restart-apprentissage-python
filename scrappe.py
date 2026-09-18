# import requests
# from bs4 import BeautifulSoup

# whith open("example.html", "r") as file :
#     soup =  BeautifulSoup(file.read(), "html.parser")

# url = "https://www.gov.uk/search/news-and-communications"

# response = requests.get(url)
# # html_code = response.text

# print(response.content)

# import requests
# from bs4 import BeautifulSoup
# from bs4 import BeautifulSoup
# with open("example.html", "r") as file:
#    soup = BeautifulSoup(file.read(), 'html.parser')

import requests
from bs4 import BeautifulSoup
from pathlib import Path

base_dir = Path(__file__).resolve().parent
file_path = base_dir / "example.html"

with open(file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file.read(), "html.parser")

print(soup.title)