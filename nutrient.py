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

    send_data = {
        'nutritionalname': menu,
        'tan': 0,
        'dan': 0,
        'ji': 0,
        'dang': 0,
        'na': 0,
        'cal': 0,
        'col': 0,
    }

    for data in data_list:
        title = data.select(
            '.info_area > .subject > .title > a > strong'
        )[0].text
        if title == f'{menu} 영양성분':
            nutrient_list = str(data.select(
                'p'
            )[0].text).replace('|', '-').replace(' ', '').replace(':', '').split('-')
            res_col = data.select(
                ' .related > .info > .data'
            )[2].text
            break
    
    check_list = ['탄수화물', '단백질', '지방', '당류', '나트륨', '콜레스테롤']
    name_list = ['tan', 'dan', 'ji', 'dang', 'na', 'col']
    check_len = 0
    
    for i in range(0, 6):
        check_len = len(check_list[i])
        for nutrient in nutrient_list[1:]:
            if check_list[i] in nutrient[:check_len]:
                num = ''
                for char in nutrient[check_len:]:
                    if char.isdigit():
                        num += char
                    else:
                        send_data[name_list[i]] = int(num)
                        break
                break
    
    num = ''
    for char in res_col:
        if char.isdigit():
            num += char
        else:
            send_data['cal'] = int(num)
            break

    return send_data
    

search_nutrient('비빔밥')
search_nutrient('잔치국수')
