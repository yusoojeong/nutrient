import requests
from bs4 import BeautifulSoup

def search_nutrient(menu):
    ## HTTP GET Request
    req = requests.get(f'https://terms.naver.com/search.nhn?query={menu}+%EC%98%81%EC%96%91%EC%84%B1%EB%B6%84&searchType=text&dicType=&subject=')
    ## HTML 소스 가져오기
    html = req.text
    ## BeautifulSoup으로 html소스를 python객체로 변환하기
    ## 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
    ## 이 글에서는 Python 내장 html.parser를 이용했다.
    soup = BeautifulSoup(html, 'html.parser')