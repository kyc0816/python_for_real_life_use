# 이게 들어있는 폴더까지 cd해서 온 후
# source ../../venv/bin/activate 해서 venv 켠 뒤
# python temp_skyscanner.py 해서 실행

from Dates.datesGenerator import dateGenerator
from savedUrls import urlFirst, urlLast
from cities import cities
import webbrowser

dateGenerator = dateGenerator()
datesCombinations = dateGenerator.datesCombinations

# 단건 조회 - example
import subprocess
chrome = 'Google Chrome'

def openNewWindow(): # 새 크롬 창을 여는 함수
    subprocess.run(('/Applications/' + chrome + '.app/Contents/MacOS/' + chrome))
exampleURL1 = urlFirst['paris'] + datesCombinations[0][0] + '/' + datesCombinations[0][1] + urlLast['paris']
openNewWindow()
webbrowser.open_new(exampleURL1)

