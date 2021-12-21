import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.zoom.com.br/smart-speaker/smart-speaker-amazon-echo-dot-alexa?_lc=88&searchterm=alexa"
    session = requests.Session()
    response = session.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    price_tags = soup.find("a", attrs={"data-testid": "value-anchor"})
    print(price_tags.text)

main()