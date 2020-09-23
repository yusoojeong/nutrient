# import requests
# from bs4 import BeautifulSoup

# # HTTP GET Request
# menu = '비빔밥'
# req = requests.get(f'https://www.google.com/search?q={menu}5&sxsrf=ALeKk00ogQknujG2WLi2jETxGZXNjYeptQ:1600761147448&source=lnms&tbm=isch&sa=X&ved=2ahUKEwja-8D8o_zrAhWPHHAKHavVA7wQ_AUoAXoECBsQAw&cshid=1600761157852935&biw=1536&bih=754')

# # HTML 소스 가져오기
# html = req.text
# # # HTTP header
# # header = req.headers
# # # HTTP Status
# # status = req.status_code
# # # HTTP 정상 동작 여부 (T/F)
# # is_ok = req.ok


# ## BeautifulSoup으로 html소스를 python객체로 변환하기
# ## 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
# ## 이 글에서는 Python 내장 html.parser를 이용했다.
# soup = BeautifulSoup(html, 'html.parser')

# ## image들을 가져오자
# images = soup.select(
#     '#islrg > div.islrc > a.wXeWr.islib.nfEiy.mM5pbd > div.bRMDJf.islir > img'
# )

# print(images)
