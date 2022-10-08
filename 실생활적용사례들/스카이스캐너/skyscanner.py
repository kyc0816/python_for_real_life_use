# 이게 들어있는 폴더까지 cd해서 온 후
# source ../../venv/bin/activate 해서 venv 켠 뒤
# python temp_skyscanner.py 해서 실행

from datesGenerator import dataGenerator
from savedUrls import urlFirst, urlLast
from cities import cities
import webbrowser

dataGenerator = dataGenerator()
datesCombinations = dataGenerator.datesCombinations

# FINAL (도시 1개, 날짜 20개, 한 창에 10개씩)

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

