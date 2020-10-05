from urllib.request import urlretrieve    # 이미지 저장에 유용함
from urllib.parse import quote_plus  # 한글을 컴퓨팅 언어로 바꿔줌
from bs4 import BeautifulSoup   # 크롤링에 필요한 필수 라이브러리 
from selenium import webdriver   

search = input("원하는 사진: ")
url = f'https://www.google.com/search?q={quote_plus(search)}&tbm=isch&ved=2ahUKEwjbt5OehpHsAhUJ4pQKHRAKDlsQ2-cCegQIABAC&oq=%EC%9C%A0%EC%95%84&gs_lcp=ChJtb2JpbGUtZ3dzLXdpei1pbWcQA1AAWABg3b4RaABwAHgAgAEAiAEAkgEAmAEA&sclient=mobile-gws-wiz-img&ei=n5B0X5vsGonE0wSQlLjYBQ&bih=1198&biw=1197'

driver = webdriver.Chrome(r"C:\Users\multicampus\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(url)
for i in range(500):
    driver.execute_script("window.scrollBy(0,10000)")

html = driver.page_source
soup = BeautifulSoup(html)

img = soup.select('.rg_i.Q4LuWd')
n = 1
imgurl = []
for i in img:
    try:
        imgurl.append(i.attrs["src"])
    except KeyError:
        imgurl.append(i.attrs["data-src"])

for i in imgurl:
    urlretrieve(i, f"downloads/" + search + str(n) + ".jpg")
    n += 1

driver.close()