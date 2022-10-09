# 이게 들어있는 폴더까지 cd해서 온 후
# source ../../venv/bin/activate 해서 venv 켠 뒤
# python temp_skyscanner.py 해서 실행

from Dates.datesGenerator import dateGenerator
from savedUrls import urlFirst, urlLast
from cities import cities
import webbrowser

dateGenerator = dateGenerator()
datesCombinations = dateGenerator.datesCombinations

# # 1 - requests 사용 - 실패 (한 번에 불러올 수 있는 구조가 아니고, 억지로 nest로 불러오려하면 5XX 에러 뜸.)
# response = requests.get('https://www.skyscanner.co.kr/transport/flights/icn/pari/221020/221121/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27539733&inboundaltsenabled=false&infants=0&originentityid=27538638&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1')
# html = response.text
# print(html)

# # 2 - 웹브라우저에 띄우자. (example 1 - 단건)
# # ** new = 0 하면 새 창이 아니라 같은 창에 새 탭으로 띄움. ** 근데 1이나 2 해도 마찬가지.. 새 창은 이거로 안되고 subprocess 써야된다.
# exampleURL1 = urlFirst['paris'] + datesCombinations[0][0] + '/' + datesCombinations[0][1] + urlLast['paris']
# # # 아래 세 줄은 구글 크롬 새 브라우저 띄우는 코드임.
# # import subprocess
# # chrome = 'Google Chrome'
# # subprocess.run(('/Applications/' + chrome + '.app/Contents/MacOS/' + chrome))
# webbrowser.open_new(exampleURL1)


# 3 - 웹브라우저에 띄우자. (example 2 - 도시 1개, 날짜 20개, 한 창에 10개씩)
# 전체 날짜 조합 갯수, 그리고 한 번에 열 조합의 갯수 (=크롬 탭의 갯수)
numberOfTotalDatesCombinations = len(datesCombinations) # 3081
numberOfTargetDatesCombinations = 20

import subprocess
chrome = 'Google Chrome'

def openNewWindow(): # 새 크롬 창을 여는 함수
    subprocess.run(('/Applications/' + chrome + '.app/Contents/MacOS/' + chrome))

def return1on10s(n): # n이 10의 배수일때만 1을 리턴하는 함수
    if n%10 == 0:
        return 1
    else:
        return 0

def exampleRun2(cityName, startIndex):
    urlFirst2 = urlFirst[cityName]
    urlLast2 = urlLast[cityName]
    for i in range(startIndex, startIndex+20):
        tempURL = urlFirst2 + datesCombinations[i][0] + '/' + datesCombinations[i][1] + urlLast2
        if return1on10s(i)==1:
            openNewWindow()
        webbrowser.open(tempURL, 0)
        if (i == 3080):
            break

# 현재 몇개 처리했는지 가져오고, 거기에 20을 더해서 덮어쓰기. (한 번에 20개씩 할거니까.)
f = open('./static/datesCombinationsAlreadyHandled.txt', 'r')
datesCombinationsAlreadyHandled = f.readline()
f.close()

for city in cities:
    exampleRun2(city, int(datesCombinationsAlreadyHandled))

newDatesCombinationsAlreadyHandled = int(datesCombinationsAlreadyHandled) + 20
f = open('./static/datesCombinationsAlreadyHandled.txt', 'w')
f.write(str(newDatesCombinationsAlreadyHandled))
f.close()

# 4 - 모두

