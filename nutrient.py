import requests
from bs4 import BeautifulSoup

def search_nutrient(menu):
    ## HTTP GET Request
    req = requests.get(f'https://terms.naver.com/search.nhn?query={menu}+%EC%98%81%EC%96%91%EC%84%B1%EB%B6%84&searchType=text&dicType=&subject=')

    ## BeautifulSoup으로 html소스를 python객체로 변환하기
    res = BeautifulSoup(req.text, 'html.parser')
    data_list = res.select(
        '#content > .search_result_area'
    )

    for data in data_list:
        title = data.select(
            '.info_area > .subject > .title > a > strong'
        )[0].text
        if title == f'{menu} 영양성분':
            nutrient_list = str(data.select(
                'p'
            )[0].text).replace('|', '-').replace(' ', '').replace(':', '').split('-')
            print(nutrient_list)
            res_col = data.select(
                ' .related > .info > .data'
            )[2].text
            print(res_col)
            break

    print("=================")
    

search_nutrient('비빔밥')
search_nutrient('잔치국수')
