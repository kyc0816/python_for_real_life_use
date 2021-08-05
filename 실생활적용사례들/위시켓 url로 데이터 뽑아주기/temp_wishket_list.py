# 이게 들어있는 폴더까지 cd해서 온 후
# source ../venv/bin/activate 해서 venv 켠 뒤
# python temp_wishket_list.py 해서 실행

# https://www.lesstif.com/software-architect/curl-http-get-post-rest-api-14745703.html
# https://somjang.tistory.com/entry/Python-Python3%EC%97%90%EC%84%9C-venv%EB%A1%9C-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-%EB%A7%8C%EB%93%A4%EA%B3%A0-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

# https://stackoverflow.com/a/65802367 --> # import 빨간줄떠서 커맨드 팔레트(cmd shift P 혹은 fn F1)에서 Developer: Reload Window로 새로고침 해주니 해결됨
import requests
from bs4 import BeautifulSoup
# https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/

urlsMenu = {0: '(예시) 위시켓 첫 10개의 프로젝트들', 1: '210723 배치도 다음 작업 살펴보기', 2: '210731 배치도 다음 작업 살펴보기'}
toShow = [0, 1, 2] # urlsMenu 중에서 실제로 선택지로 줄 것들의 번호

print('\n아래 리스트에서 보고싶은 url 뭉치의 번호를 입력해주세요 (숫자만 입력)\n')
for key in toShow:
    print(f'{key}번 : {urlsMenu[key]}\n')
    # https://stackoverflow.com/questions/2960772/how-do-i-put-a-variable-inside-a-string # f - string

from savedURLs import urlsList
urls = ['-1']
while True:
    selectedUrlNum = input()
    if selectedUrlNum== 'q':
        break
    try:
        selectedUrlNum = int(selectedUrlNum)
        if selectedUrlNum in toShow:
            urls = urlsList[selectedUrlNum]
            break
        else:
            print('\n보여준 것들 중에서 골라주세요... (그만두려면 q를 눌러주세요)')
            urls = ['-1']
    except Exception as e:
        print('\n제대로된 숫자를 넣어주세요... (그만두려면 q를 눌러주세요)')
        urls = ['-1']

count = 1

for url in urls:
    if url == '-1':
        break
    response = requests.get(url)
    html = response.text
    # https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
    soup = BeautifulSoup(html, 'html.parser')
    # https://m.blog.naver.com/kiddwannabe/221177292446 - 3. 필요한 정보 가져오기
    print('(', count, ')')
    count+=1
    # https://stackoverflow.com/a/67099842 # 밑에 .text 이 부분마다 unknown type이라고 빨간줄 떠서 ; 아니 파이썬에서 타입을 왜 따져 ㅋㅋ
    print('제목 : ', soup.select('h1.subtitle-1-medium')[0].text) # type: ignore
    print('링크 : ', url)
    print('견적 : ', soup.select('p.project-condition-data')[0].text, ' / 기간 : ', soup.select('p.project-condition-data')[1].text) # type: ignore
    skills= []
    for skill in soup.select('div.subcategory-box'):
        skills.append(skill.text) # type: ignore
    print('관련 기술 : ', skills)
    print(' ')

# 요상한 기능이 생겼음... 이렇게 #%% 치면 그 아래로 쥬피터 노트북 뜸. 그 안에 커서 놓은채로 shift enter 하면 실행도 됨 ㅋ
#%%
print('ByE')